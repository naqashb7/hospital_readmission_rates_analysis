import streamlit as st
import pandas as pd
import joblib
 
st.title("🩺 Diabetes Readmission Prediction")
st.markdown("Enter patient details below to predict the likelihood of hospital readmission.")
st.markdown("---")
 
col1, col2, col3 = st.columns(3)
 
with col1:
    st.markdown("#### 👤 Patient Info")
    age = st.selectbox("Age Range", options=[
        "[0-10)", "[10-20)", "[20-30)", "[30-40)", "[40-50)",
        "[50-60)", "[60-70)", "[70-80)", "[80-90)", "[90-100)"
    ])
    gender = st.selectbox("Gender", options=["Male", "Female"])
    race = st.selectbox("Race", options=["AfricanAmerican", "Asian", "Caucasian", "Hispanic", "Other"])
 
    st.markdown("#### 🏥 Hospital Info")
    time_in_hospital = st.slider("Time in Hospital (days)", 1, 14, 3)
    num_lab_procedures = st.slider("Lab Procedures", 1, 132, 43)
    num_procedures = st.slider("Procedures", 0, 6, 1)
    num_medications = st.slider("Medications", 1, 81, 15)
    number_outpatient = st.slider("Outpatient Visits", 0, 42, 0)
    number_emergency = st.slider("Emergency Visits", 0, 76, 0)
    number_inpatient = st.slider("Inpatient Visits", 0, 21, 0)
 
with col2:
    st.markdown("#### 🩸 Test Results")
    max_glu_serum = st.selectbox("Max Glucose Serum", options=["None", "Norm", ">200", ">300"])
    A1Cresult = st.selectbox("A1C Result", options=["None", "Norm", ">7", ">8"])
 
    st.markdown("#### 📋 Diagnoses")
    diag_1 = st.selectbox("Primary Diagnosis", options=[
        "Circulatory", "Diabetes", "Digestive", "Endocrine",
        "Genitourinary", "Injury", "Musculoskeletal", "Neoplasms",
        "Other", "Respiratory"
    ])
    diag_2 = st.selectbox("Secondary Diagnosis", options=[
        "Circulatory", "Diabetes", "Digestive", "Endocrine",
        "Genitourinary", "Injury", "Musculoskeletal", "Neoplasms",
        "No diagnosis", "Other", "Respiratory"
    ])
    diag_3 = st.selectbox("Additional Diagnosis", options=[
        "Circulatory", "Diabetes", "Digestive", "Endocrine",
        "Genitourinary", "Injury", "Musculoskeletal", "Neoplasms",
        "No diagnosis", "Other", "Respiratory"
    ])
 
    st.markdown("#### 💊 Medication Info")
    diabetesMed = st.selectbox("On Diabetes Medication", options=["Yes", "No"])
    change = st.selectbox("Medication Change", options=["Ch", "No"])
    insulin = st.selectbox("Insulin", options=["No", "Steady", "Up", "Down"])
    metformin = st.selectbox("Metformin", options=["No", "Steady", "Up", "Down"])
    glipizide = st.selectbox("Glipizide", options=["No", "Steady", "Up", "Down"])
    glyburide = st.selectbox("Glyburide", options=["No", "Steady", "Up", "Down"])
    glimepiride = st.selectbox("Glimepiride", options=["No", "Steady", "Up", "Down"])
 
with col3:
    st.markdown("#### 💊 Other Medications")
    pioglitazone = st.selectbox("Pioglitazone", options=["No", "Steady", "Up", "Down"])
    rosiglitazone = st.selectbox("Rosiglitazone", options=["No", "Steady", "Up", "Down"])
    repaglinide = st.selectbox("Repaglinide", options=["No", "Steady", "Up"])
    nateglinide = st.selectbox("Nateglinide", options=["No", "Steady", "Up"])
    chlorpropamide = st.selectbox("Chlorpropamide", options=["No", "Steady", "Up"])
    acarbose = st.selectbox("Acarbose", options=["No", "Steady", "Up"])
    miglitol = st.selectbox("Miglitol", options=["No", "Steady", "Up"])
    tolazamide = st.selectbox("Tolazamide", options=["No", "Steady", "Up"])
    glyburide_metformin = st.selectbox("Glyburide-Metformin", options=["No", "Steady", "Up"])
 
st.markdown("---")
 
def encode_inputs():
    age_map = {
        "[0-10)": 0, "[10-20)": 1, "[20-30)": 2, "[30-40)": 3, "[40-50)": 4,
        "[50-60)": 5, "[60-70)": 6, "[70-80)": 7, "[80-90)": 8, "[90-100)": 9
    }
    glu_map = {"None": 0, "Norm": 1, ">200": 2, ">300": 3}
    a1c_map = {"None": 0, "Norm": 1, ">7": 2, ">8": 3}
 
    data = {
        "time_in_hospital": [time_in_hospital],
        "num_lab_procedures": [num_lab_procedures],
        "num_procedures": [num_procedures],
        "num_medications": [num_medications],
        "number_outpatient": [number_outpatient],
        "number_emergency": [number_emergency],
        "number_inpatient": [number_inpatient],
        "max_glu_serum": [glu_map[max_glu_serum]],
        "A1Cresult": [a1c_map[A1Cresult]],
        "gender_encoded": [1 if gender == "Male" else 0],
        "diabetesMed_encoded": [1 if diabetesMed == "Yes" else 0],
        "change_encoded": [1 if change == "Ch" else 0],
        "race_Asian": [1 if race == "Asian" else 0],
        "race_Caucasian": [1 if race == "Caucasian" else 0],
        "race_Hispanic": [1 if race == "Hispanic" else 0],
        "race_Other": [1 if race == "Other" else 0],
        "diag_1_Diabetes": [1 if diag_1 == "Diabetes" else 0],
        "diag_1_Digestive": [1 if diag_1 == "Digestive" else 0],
        "diag_1_Endocrine": [1 if diag_1 == "Endocrine" else 0],
        "diag_1_Genitourinary": [1 if diag_1 == "Genitourinary" else 0],
        "diag_1_Injury": [1 if diag_1 == "Injury" else 0],
        "diag_1_Musculoskeletal": [1 if diag_1 == "Musculoskeletal" else 0],
        "diag_1_Neoplasms": [1 if diag_1 == "Neoplasms" else 0],
        "diag_1_Other": [1 if diag_1 == "Other" else 0],
        "diag_1_Respiratory": [1 if diag_1 == "Respiratory" else 0],
        "diag_2_Diabetes": [1 if diag_2 == "Diabetes" else 0],
        "diag_2_Digestive": [1 if diag_2 == "Digestive" else 0],
        "diag_2_Endocrine": [1 if diag_2 == "Endocrine" else 0],
        "diag_2_Genitourinary": [1 if diag_2 == "Genitourinary" else 0],
        "diag_2_Injury": [1 if diag_2 == "Injury" else 0],
        "diag_2_Musculoskeletal": [1 if diag_2 == "Musculoskeletal" else 0],
        "diag_2_Neoplasms": [1 if diag_2 == "Neoplasms" else 0],
        "diag_2_No diagnosis": [1 if diag_2 == "No diagnosis" else 0],
        "diag_2_Other": [1 if diag_2 == "Other" else 0],
        "diag_2_Respiratory": [1 if diag_2 == "Respiratory" else 0],
        "diag_3_Diabetes": [1 if diag_3 == "Diabetes" else 0],
        "diag_3_Digestive": [1 if diag_3 == "Digestive" else 0],
        "diag_3_Endocrine": [1 if diag_3 == "Endocrine" else 0],
        "diag_3_Genitourinary": [1 if diag_3 == "Genitourinary" else 0],
        "diag_3_Injury": [1 if diag_3 == "Injury" else 0],
        "diag_3_Musculoskeletal": [1 if diag_3 == "Musculoskeletal" else 0],
        "diag_3_Neoplasms": [1 if diag_3 == "Neoplasms" else 0],
        "diag_3_No diagnosis": [1 if diag_3 == "No diagnosis" else 0],
        "diag_3_Other": [1 if diag_3 == "Other" else 0],
        "diag_3_Respiratory": [1 if diag_3 == "Respiratory" else 0],
        # Medications
        "metformin_No": [1 if metformin == "No" else 0],
        "metformin_Steady": [1 if metformin == "Steady" else 0],
        "metformin_Up": [1 if metformin == "Up" else 0],
        "repaglinide_No": [1 if repaglinide == "No" else 0],
        "repaglinide_Steady": [1 if repaglinide == "Steady" else 0],
        "repaglinide_Up": [1 if repaglinide == "Up" else 0],
        "nateglinide_No": [1 if nateglinide == "No" else 0],
        "nateglinide_Steady": [1 if nateglinide == "Steady" else 0],
        "nateglinide_Up": [1 if nateglinide == "Up" else 0],
        "chlorpropamide_No": [1 if chlorpropamide == "No" else 0],
        "chlorpropamide_Steady": [1 if chlorpropamide == "Steady" else 0],
        "chlorpropamide_Up": [1 if chlorpropamide == "Up" else 0],
        "glimepiride_No": [1 if glimepiride == "No" else 0],
        "glimepiride_Steady": [1 if glimepiride == "Steady" else 0],
        "glimepiride_Up": [1 if glimepiride == "Up" else 0],
        "acetohexamide_Steady": [0],  
        "glipizide_No": [1 if glipizide == "No" else 0],
        "glipizide_Steady": [1 if glipizide == "Steady" else 0],
        "glipizide_Up": [1 if glipizide == "Up" else 0],
        "glyburide_No": [1 if glyburide == "No" else 0],
        "glyburide_Steady": [1 if glyburide == "Steady" else 0],
        "glyburide_Up": [1 if glyburide == "Up" else 0],
        "tolbutamide_Steady": [0],  
        "pioglitazone_No": [1 if pioglitazone == "No" else 0],
        "pioglitazone_Steady": [1 if pioglitazone == "Steady" else 0],
        "pioglitazone_Up": [1 if pioglitazone == "Up" else 0],
        "rosiglitazone_No": [1 if rosiglitazone == "No" else 0],
        "rosiglitazone_Steady": [1 if rosiglitazone == "Steady" else 0],
        "rosiglitazone_Up": [1 if rosiglitazone == "Up" else 0],
        "acarbose_No": [1 if acarbose == "No" else 0],
        "acarbose_Steady": [1 if acarbose == "Steady" else 0],
        "acarbose_Up": [1 if acarbose == "Up" else 0],
        "miglitol_No": [1 if miglitol == "No" else 0],
        "miglitol_Steady": [1 if miglitol == "Steady" else 0],
        "miglitol_Up": [1 if miglitol == "Up" else 0],
        "troglitazone_Steady": [0],       
        "tolazamide_Steady": [1 if tolazamide == "Steady" else 0],
        "tolazamide_Up": [1 if tolazamide == "Up" else 0],
        "insulin_No": [1 if insulin == "No" else 0],
        "insulin_Steady": [1 if insulin == "Steady" else 0],
        "insulin_Up": [1 if insulin == "Up" else 0],
        "glyburide-metformin_No": [1 if glyburide_metformin == "No" else 0],
        "glyburide-metformin_Steady": [1 if glyburide_metformin == "Steady" else 0],
        "glyburide-metformin_Up": [1 if glyburide_metformin == "Up" else 0],
        "glipizide-metformin_Steady": [0],       
        "glimepiride-pioglitazone_Steady": [0],  
        "metformin-pioglitazone_Steady": [0],    
        "age_encoded": [age_map[age]],
    }
 
    column_order = [
        "time_in_hospital", "num_lab_procedures", "num_procedures", "num_medications",
        "number_outpatient", "number_emergency", "number_inpatient",
        "max_glu_serum", "A1Cresult",
        "gender_encoded", "diabetesMed_encoded", "change_encoded",
        "race_Asian", "race_Caucasian", "race_Hispanic", "race_Other",
        "diag_1_Diabetes", "diag_1_Digestive", "diag_1_Endocrine", "diag_1_Genitourinary",
        "diag_1_Injury", "diag_1_Musculoskeletal", "diag_1_Neoplasms", "diag_1_Other", "diag_1_Respiratory",
        "diag_2_Diabetes", "diag_2_Digestive", "diag_2_Endocrine", "diag_2_Genitourinary",
        "diag_2_Injury", "diag_2_Musculoskeletal", "diag_2_Neoplasms", "diag_2_No diagnosis",
        "diag_2_Other", "diag_2_Respiratory",
        "diag_3_Diabetes", "diag_3_Digestive", "diag_3_Endocrine", "diag_3_Genitourinary",
        "diag_3_Injury", "diag_3_Musculoskeletal", "diag_3_Neoplasms", "diag_3_No diagnosis",
        "diag_3_Other", "diag_3_Respiratory",
        "metformin_No", "metformin_Steady", "metformin_Up",
        "repaglinide_No", "repaglinide_Steady", "repaglinide_Up",
        "nateglinide_No", "nateglinide_Steady", "nateglinide_Up",
        "chlorpropamide_No", "chlorpropamide_Steady", "chlorpropamide_Up",
        "glimepiride_No", "glimepiride_Steady", "glimepiride_Up",
        "acetohexamide_Steady",
        "glipizide_No", "glipizide_Steady", "glipizide_Up",
        "glyburide_No", "glyburide_Steady", "glyburide_Up",
        "tolbutamide_Steady",
        "pioglitazone_No", "pioglitazone_Steady", "pioglitazone_Up",
        "rosiglitazone_No", "rosiglitazone_Steady", "rosiglitazone_Up",
        "acarbose_No", "acarbose_Steady", "acarbose_Up",
        "miglitol_No", "miglitol_Steady", "miglitol_Up",
        "troglitazone_Steady",
        "tolazamide_Steady", "tolazamide_Up",
        "insulin_No", "insulin_Steady", "insulin_Up",
        "glyburide-metformin_No", "glyburide-metformin_Steady", "glyburide-metformin_Up",
        "glipizide-metformin_Steady",
        "glimepiride-pioglitazone_Steady",
        "metformin-pioglitazone_Steady",
        "age_encoded"
    ]
 
    return pd.DataFrame(data)[column_order]
 
 
if st.button("Predict Readmission Risk"):
    input_df = encode_inputs()
 
    model = joblib.load("model/lr_model.pkl")   
    scaler = joblib.load("model/scaler.pkl") 
 
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]
 
    st.markdown("---")
 
    if prediction == 1:
        st.error(f"⚠️ High Readmission Risk Detected — Probability: {probability:.1%}")
        st.markdown("This patient has an elevated risk of readmission. Consider reviewing their treatment plan and follow-up care.")
    else:
        st.success(f"✅ Low Readmission Risk — Probability: {probability:.1%}")
        st.markdown("This patient currently shows a low risk of hospital readmission.")
 
    st.warning("⚠️ This is not official medical advice and should not replace professional clinical judgement. If you have concerns about a patient, please seek appropriate medical guidance.")
 