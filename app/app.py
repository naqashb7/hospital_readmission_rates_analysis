import streamlit as st
import os

st.set_page_config(
    page_title="Diabetic Patient Readmission Prediction App",
    page_icon="💉",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title("💉 Diabetic Patient Readmission Prediction App")
st.sidebar.markdown("---")
st.sidebar.markdown("### About")
st.sidebar.markdown("This app predicts the likelihood of diabetes patients being readmitted to hospital based off of historic health data. Explore the navigation menu above to learn more! \n\n**DISCLAIMER:** The predictions made from this app are purely theoretical. Do not accept it as official medical advice. If you have any concerns about your health, seek help from a medical professional immediately!")

BASE_DIR = os.getcwd()  

intro = st.Page(os.path.join(BASE_DIR, "pages", "1_Intro.py"), title="Introduction", icon="🏥")
dataset = st.Page(os.path.join(BASE_DIR, "pages", "2_Data.py"), title="Dataset", icon="📊")
visuals = st.Page(os.path.join(BASE_DIR, "pages", "3_Visualisations.py"), title="Visualisations", icon="🔍")
model = st.Page(os.path.join(BASE_DIR, "pages", "4_MLModel.py"), title="Modelling and Evaluation", icon="🤖")
prediction = st.Page(os.path.join(BASE_DIR, "pages", "5_Predictor.py"), title="Patient Readmission Prediction", icon="🩺")
ethics = st.Page(os.path.join(BASE_DIR, "pages", "6_Ethical_Considerations.py"), title="Ethical Considerations", icon="⚖️")

pg = st.navigation([intro, dataset, visuals, model, prediction, ethics])
pg.run()