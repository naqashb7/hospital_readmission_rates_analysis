import streamlit as st
import pandas as pd

st.title("📊 Dataset Overview")

df = pd.read_csv("data_files/ModellingData/modelling_hospital_data.csv")


st.markdown("""

## Summary of Dataset

""")
col1, col2, col3 = st.columns(3)
col1.metric("Total Records", df.shape[0])
col2.metric("Total Features (post encoding)", df.shape[1])
col3.metric("Readmitted Cases", df["readmitted"].sum())

st.markdown("---")
st.markdown("""

## Snapshot of Modelling Dataset

Below is a snapshot of the Modelling dataset. This was created after the ETL pipeline and prior to removal of the non-encoded categorical fields.            


""")

st.subheader("Modelling Data Sample")
st.dataframe(df.head(20))

st.markdown("---")
st.markdown("""

## Statistical Analysis of Dataset

Below is a summary statistical analysis of the Modelling dataset.

""")
st.dataframe(df.describe())

st.markdown("---")
st.markdown("""

## Analysis of Null Values

Below is an analysis of null values within the Modelling dataset. As can be seen, post ETL, all null values had been removed.            


""")
st.subheader("Missing Values")
missing = df.isnull().sum().reset_index()
missing.columns = ["Feature", "Missing Values"]
st.dataframe(missing)

st.markdown("---")

st.markdown("""

## Distribution of Classes

Below is a summary of the distributions of the majority class (Not Readmitted) and minority class(Readmitted) in the Modelling dataset.            


""")
col1, col2 = st.columns(2)
col1.metric("Not Readmitted (0)", df[df["readmitted"] == 0].shape[0])
col2.metric("Readmitted (1)", df[df["readmitted"] == 1].shape[0])