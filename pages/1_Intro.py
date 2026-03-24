import streamlit as st

st.title("🏥 Introduction")
st.markdown("""
## App Overview
This app looks to predict the likelihood of individuals with diabetes being readmitted to hospital. It explores different illnesses diabetes patients may have, their backgrounds and readmittance rates
using a dataset of historic health and demographic information. 
            
---
            
## Background
Diabetes patients being readmitted to hospital has been a big strain on healthcare systems. It can be very expensive so readmitting a patient can cost lots of money.
By being able to predict why a patient is being readmitted, we can figure out ways to prevent readmission and tackle the issue at source.
---

## Dataset background
- **Source:** [Diabetes 130 US hospitals for years 1999-2008 Dataset](https://www.kaggle.com/datasets/brandao/diabetes) from Kaggle
- **Records:** ~100,000 records
- **Target Variable:** Readmitted (0 = Not readmitted or Readmitted More than 30 days after discharge, 1 = Readmitted less than 30 days after discharge))
- **Other Variables:**
    - Age
    - Gender 
    - Race
    - Weight
    - Admission type
    - Number of lab and non lab procedures
    - Primary, Secondary & Tertiary  Diagnoses
    - Blood Sugar testing
    - Medicinal Changes

---
            
## Key Findings
- Age was given the greatest weight as a predictor of stroke occurrence
- Higher average glucose levels had a strong relationship with increased stroke risk
- Individuals with medical histories that included hypertension and heart disease showed higher stroke rates

---            

## Full Project Process
1. ETL pipeline
2. Exploratory Data Analysis (EDA)
3. Machine Learning Pipeline
4. Predictive App and dashboard design and deployment

---            
## Hypotheses
            
1) Age: 
    * H<sub>0</sub>: Age has no impact on diabetes patient readmittance rates to hospital.
2) Race:
    * H<sub>0</sub>: Race has no impact on diabetes patient readmittance rates to hospital.
3) Gender:
    * H<sub>0</sub>: Gender has no impact on diabetes patient readmittance rates to hospital.
4) Time in hospital:
    * H<sub>0</sub>: Time spent in hospital during a patient's latest encounter, has no impact on diabetes patient readmittance rates to hospital.
5) Number of medications:
    * H<sub>0</sub>: Number of medications administered during a patient's latest encounter, has no impact on diabetes patient readmittance rates to hospital.
6) Number of Lab procedures:
    * H<sub>0</sub>: Number of lab procedures performed during a patient's latest encounter, has no impact on diabetes patient readmittance rates to hospital.
7) Number of Non-lab procedures:
    * H<sub>0</sub>: Number of non-lab procedures performed during a patient's latest encounter, has no impact on diabetes patient readmittance rates to hospital.
8) Prior Visit History:
    * H<sub>0</sub>: The type of prior visits a patient does (Inpatient, Outpatient, Emergency) over the last year, has no impact on diabetes patient readmittance rates to hospital.
9) Diagnosis type:
    * H<sub>0</sub>: The type of diagnoses during a patient's latest encounter, has no impact on diabetes patient readmittance rates to hospital.
10) Medicinal Changes:
    * H<sub>0</sub>: Any Medicinal changes during a patient's latest encounter, has no impact on diabetes patient readmittance rates to hospital.
11) Testing performed:
    * H<sub>0</sub>: Blood testing performed during a patient's latest encounter, has no impact on diabetes patient readmittance rates to hospital.

            

---

## Conclusions


1) Age: 
    * H<sub>0</sub>: Age has no impact on diabetes patient readmittance rates to hospital.
        * The analysis above shows that as a patient gets older, they tend to spend more time in hospital and are more likely to be readmitted.
        * The Null hypothesis can be rejected.
        * The reasoning for this could be due to weaker immune systems in older patients.
2) Race:
    * H<sub>0</sub>: Race has no impact on diabetes patient readmittance rates to hospital.
        * The analysis shows that African-American patients spent the most time in hospital while Asian patients spent the least time.
        * Asian patients were also the least readmitted to hospital.
        * There is a clear discrepancy seen in the data amongst races.
        * This means that the null hypothesis can be rejected.
3) Gender:
    * H<sub>0</sub>: Gender has no impact on diabetes patient readmittance rates to hospital.
        * There was no clear significant difference in readmittance rates between males and females.
        * The null hypothesis can not be rejected.
4) Time in hospital:
    * H<sub>0</sub>: Time spent in hospital during a patient's latest encounter, has no impact on diabetes patient readmittance rates to hospital.
        * From the heatmap analysis, it is clear that the longer a patient had spent in hospital, the more likely they were to be readmitted, whether it was less than or more than 30 days later.
        * It is also seen that patients who were readmitted to hospital had a mean stay of 4 days while those who did not had a mean stay of 3 days.
        * Considering both previous analyses, the null hypothesis can be rejected.
5) Number of medications:
    * H<sub>0</sub>: Number of medications administered during a patient's latest encounter, has no impact on diabetes patient readmittance rates to hospital.
        * There was a slight higher number of medications administered to patients that were readmitted to the hospital over those who were not.
        * However, there was large variablity in the data and a lot of outliers so the data is not reliable.
        * For this reason, the null hypothesis can not be rejected.
6) Number of Lab procedures:
    * H<sub>0</sub>: Number of lab procedures performed during a patient's latest encounter, has no impact on diabetes patient readmittance rates to hospital.
        * There was no significant difference in readmittance vs no readmittance when looking at the number of lab procedures the patient had gone through in their previous encounter.
        * Additional to this, there were lots of outliers in the data which indicated high variability and so low reliability.
        * Considering this, the null hypothesis can not be rejected.
7) Number of Non-lab procedures:
    * H<sub>0</sub>: Number of non-lab procedures performed during a patient's latest encounter, has no impact on diabetes patient readmittance rates to hospital.
        * There was no significant difference between readmitted patients and non-readmitted patients when looking at the number of non-lab procedures performed.
        * The null hypothesis can not be rejected.
8) Prior Visit History:
    * H<sub>0</sub>: The type of prior visits a patient does (Inpatient, Outpatient, Emergency) over the last year, has no impact on diabetes patient readmittance rates to hospital.
        * The type of prior visits a patient had in the year preceding the hospital encounter had a direct impact on the readmittance likelihood of the patient.
        * Emergency visits indicated the highest patient readmittance rate at 64%.
        * Emergency visits also indicated the highest patient readmittance rate for both Less than 30 days and more than 30 days.
        * The null hypothesis can be rejected.
9) Diagnosis type:
    * H<sub>0</sub>: The type of diagnoses during a patient's latest encounter, has no impact on diabetes patient readmittance rates to hospital.
        * When Diabetes was the primary diagnosis it had the highest readmittance rates.
        * Genitourinary diagnoses were consistently amongst the highest for readmittance rates in secondary and tertiary diagnoses.
        * This showed that different diagnoses had differing impacts on patient readmittance and so showed a connection.
        * The null hypothesis can be rejected.
10) Medicinal Changes:
    * H<sub>0</sub>: Any Medicinal changes during a patient's latest encounter, has no impact on diabetes patient readmittance rates to hospital.
        * There was a 7% increase in patients who were prescribed diabetes medication being readmitted to hospital over those who were not.
        * This indicated that there may have been errors in the prescribing of patients which then meant patients would be readmitted to hospital.
        * Further to this, the deep analysis of different diabetes medication showed:
            * Metformin and Insulin were the most commonly prescribed medications.
            * Metformin experienced no changes amongst patients, but Insulin did.
            * Where there were changes made to Insulin dosages, readmittance rates were lower.
            * Where Insulin was either not prescribed or the dosage was kept steady, readmittance rates were higher.
        * Based off of this, the null hypothesis will be rejected.
11) Testing performed:
    * H<sub>0</sub>: Blood testing performed during a patient's latest encounter, has no impact on diabetes patient readmittance rates to hospital.
        * There were two tests performed:
            * Max Glucose Serum
                * In patients where Measurement>300, readmittance rates were highest.
                * In patients where no test was performed, readmittance was higher than the normal measurement but only by 1%
            * HbA1C testing
                * In patients where Measurement>8, readmittance rates were highest.
                * However, the same rates were seen for patients where no test was performed.
        * Based off of this analysis, the null hypothesis can be rejected.

---
## Machine Learning Summary
2 ML models were tested to see which would work best in predicting readmission rates:

    -Logistic Regression
    -Random Forest

The Logistic Regression model was selected as the most suitable model 
for stroke prediction, achieving a recall of 0.50 for stroke cases and an accuracy of 0.66.            
            
            
""", unsafe_allow_html=True)