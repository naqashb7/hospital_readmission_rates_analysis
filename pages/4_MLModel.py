import streamlit as st
import pandas as pd
import joblib
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
import matplotlib.pyplot as plt

st.title("🤖 Modelling and Model Evaluation")


lr_model = joblib.load("model/lr_model.pkl")
X_test = pd.read_csv("model/X_test.csv")
y_test = pd.read_csv("model/y_test.csv")

st.subheader("Machine Learning Pipeline")
st.markdown(""" This project involved a Machine learning pipeline. The process was selected to fit the project which was using <mark style='background-color: #FF6B6B; color: white;'>*SUPERVISED LEARNING*</mark> 
            and would need <mark style='background-color: #FF6B6B; color: white;'>*CLASSIFICATION*</mark> modelling as the target variable was a binary. \n
            The pipeline was set out as follows:
1) ETL - encoding of the categorical string data was required and then the creation of a modelling dataframe
2) Define the Features and the Target - It was essential to define what the features were and what the target was
3) Train-Test Split - This stage defined the how much of the data would be split between training the model and testing the model
4) Class Imbalance - There was a class imbalance so it was important to analyse and address this
5) Scaling - To prevent variables having too much weight over others, scaling was required to balance this out
6) Training of Models - Once everything else was done, it was time to train the models.
7) Model Evaluation - After training, it was paramount to evaluate the models to then decide which model was best to use for predictive analytics for this data
""", unsafe_allow_html=True)

st.markdown("---")
st.subheader("Model Selected: Logistic Regression")
st.markdown("""
## Why Logistic Regression?
Three models were evaluated:
- Logistic Regression
- Random Forest
            


After evaluating three models, Logistic Regression was selected because:
- It showed the highest **recall of 0.50** for readmitted records - catching ~1000 out of ~2000 actual readmittance records even though its accuracy was the lowest of the two at 0.66
- The Random Forest models achieved 0.00 recall for readmitted records - This was even though it's accuracy was ~ 0.9
- Recall was an important measure, especially from a medical perspective as it was more important for the model to be able to identify patients being readmitted to hospital.
- This meant it was the most appropriate for **binary medical classification**
- It was also the most interpretable model - this is important in a healthcare context
""")

st.markdown("---")


st.subheader("Model Comparison")
st.info("""Each Model was assessed against a variety of criteria: 
- Accuracy - this measures how accurate each model was against the dataset
- Recall - this measures how many of the actual strokes documented were caught by the model
- F1-score - this calculates the balance of Precision and Recall. A high F1 score means that the model is really good with high precision and high recall.""")

comparison_df = pd.DataFrame({
    "Model": ["Logistic Regression", "Random Forest"],
    "Accuracy": [0.66, 0.89],
    "Readmitted Record Recall": [0.50, 0.00],
    "Readmitted Record F1": [0.25, 0.01]
})
st.dataframe(comparison_df, use_container_width=True)
st.info("""This is what the results displayed for each model:
* Logistic Regression model:
    * This model showed an overall accuracy of 66%
    * The Precision at predicting readmission was 16%
    * The Recall at identifying real readmission records was 50%
    * The F1-score was about 25%
    * Overall, the model was good at recalling and identifying true readmission records but had very low precision.
* Random Forest model:
    * This model showed an overall accuracy of 89%
    * The Precision was 45%
    * The Recall was 0%
    * The F1-score was 1%
    * Overall, this model was much better at precisely at predicting and identifying "Readmitted = Yes" scenarios however, it had poor recall and f1 scores. The reason this model had an accuracy of 89% was that it was able to identify "Readmitted= No" scenarios. This means that the accuracy result of this model is not reliable, especially in this case as it is important for the evaluation scores to be higher for the "Readmitted = Yes" section.
""")
st.markdown("---")


st.subheader("Logistic Regression Classification Report")
st.markdown("A comparison of the Logistic Regression model against both classes in the dataset.")
report_df = pd.DataFrame({
    "Class": ["Not Readmitted (0)", "Readmitted (1)"],
    "Precision": [0.91, 0.16],
    "Recall": [0.68, 0.50],
    "F1 Score": [0.78, 0.25],
    "Support": [17662, 2233]
})
st.dataframe(report_df, use_container_width=True)

st.markdown("---")


st.subheader("Key Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Accuracy", "0.66")
col2.metric("Stroke Recall", "0.50")
col3.metric("Stroke Precision", "0.16")
col4.metric("Stroke F1", "0.25")

st.markdown("---")


st.subheader("Confusion Matrix")
st.markdown("""The Confusion matrix help assess a models abilities for comparing predicted values against true values. The confusion matrix shows:

- 1-1 : True Positives
- 1-0 : False Negatives
- 0-1 : False Positives
- 0-0 : True Negatives
""")
y_pred = lr_model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
fig, ax = plt.subplots(figsize=(6, 5))
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(ax=ax)
ax.set_title("Logistic Regression Confusion Matrix")
st.pyplot(fig)