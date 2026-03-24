import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
 
st.sidebar.title("🔽 Filter Data")
 
df = pd.read_csv("data_files/CleanData/clean_hospital_data.csv")
 
st.sidebar.header("Filter the data and display it on the visualisations")
 

gender_filter = st.sidebar.multiselect(
    "Gender",
    options=df["gender"].unique(),
    default=df["gender"].unique()
)
 

age_ranges = sorted(df["age"].unique().tolist(), key=lambda x: int(''.join(filter(str.isdigit, x.split("-")[0])) or 0))
age_filter = st.sidebar.multiselect(
    "Age Range",
    options=age_ranges,
    default=age_ranges
)
 

race_filter = st.sidebar.multiselect(
    "Race",
    options=df["race"].unique(),
    default=df["race"].unique()
)
 

readmitted_filter = st.sidebar.multiselect(
    "Readmitted",
    options=df["readmitted"].unique(),
    default=df["readmitted"].unique()
)
 

diabetesMed_filter = st.sidebar.multiselect(
    "On Diabetes Medication",
    options=df["diabetesMed"].unique(),
    default=df["diabetesMed"].unique()
)
 

filtered_df = df[
    (df["gender"].isin(gender_filter)) &
    (df["age"].isin(age_filter)) &
    (df["race"].isin(race_filter)) &
    (df["readmitted"].isin(readmitted_filter)) &
    (df["diabetesMed"].isin(diabetesMed_filter))
]
 

st.title("🩺 Diabetes Dashboard")
st.write(f"Showing {len(filtered_df)} records")
st.info("Use the filters on the left to explore how different variables relate to diabetes outcomes.")
st.markdown("---")
 

st.subheader("🖱️ Interactive: Age Range vs Time in Hospital")
st.info("""
Explore how age ranges relate to time spent in hospital.
Each dot represents a patient — use filters to compare groups.
""")
fig = px.strip(
    filtered_df,
    x="age",
    y="time_in_hospital",
    color="readmitted",
    labels={"age": "Age Range", "time_in_hospital": "Time in Hospital (days)", "readmitted": "Readmitted"},
    title="Age Range vs Time in Hospital by Readmission Status",
    category_orders={"age": age_ranges}
)
st.plotly_chart(fig, use_container_width=True)
st.markdown("---")
 

st.subheader("A1C Result vs Readmission")
fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.countplot(data=filtered_df, x="A1Cresult", hue="readmitted", palette="Set2", ax=ax1)
ax1.set_title("A1C Result vs Readmission")
ax1.set_xlabel("A1C Result")
ax1.set_ylabel("Count")
st.pyplot(fig1)
st.info("This chart shows the distribution of A1C test results (Blood sugar testing) and how they relate to readmission rates.")
st.markdown("---")
 

st.subheader("Max Glucose Serum vs Readmission")
fig2, ax2 = plt.subplots(figsize=(8, 5))
sns.countplot(data=filtered_df, x="max_glu_serum", hue="readmitted", palette="Set2", ax=ax2)
ax2.set_title("Max Glucose Serum vs Readmission")
ax2.set_xlabel("Max Glucose Serum")
ax2.set_ylabel("Count")
st.pyplot(fig2)
st.info("Higher glucose serum levels may be associated with increased readmission rates.")
st.markdown("---")
 

st.subheader("📊 Clinical Analysis")
col1, col2 = st.columns(2)
 
with col1:
    fig4, ax4 = plt.subplots(figsize=(6, 5))
    med_summary = filtered_df.groupby("diabetesMed")["time_in_hospital"].mean()
    ax4.bar(med_summary.index, med_summary.values, color=["steelblue", "salmon"], edgecolor="black")
    ax4.set_ylabel("Avg Time in Hospital (days)")
    ax4.set_title("Diabetes Medication vs Avg Hospital Stay")
    st.pyplot(fig4)
 
with col2:
    fig5, ax5 = plt.subplots(figsize=(6, 5))
    sns.violinplot(data=filtered_df, x="readmitted", y="num_medications", palette="Set2", inner="quartile", ax=ax5)
    ax5.set_title("Number of Medications by Readmission")
    ax5.set_xlabel("Readmitted")
    ax5.set_ylabel("Number of Medications")
    st.pyplot(fig5)
 
st.info("""
- Patients prescribed diabetes medication on their hospital encounters show longer hospital stay durations.
- The number of medications prescribed varies slightly between readmitted and non-readmitted patients.
""")
st.markdown("---")
 

st.subheader("Insulin Usage vs Readmission")
col3, col4 = st.columns(2)
 
with col3:
    fig6, ax6 = plt.subplots(figsize=(6, 5))
    sns.countplot(data=filtered_df, x="insulin", hue="readmitted", palette="Set2", ax=ax6)
    ax6.set_title("Insulin vs Readmission")
    ax6.set_xlabel("Insulin")
    ax6.set_ylabel("Count")
    plt.xticks(rotation=45)
    st.pyplot(fig6)
 
with col4:
    fig7, ax7 = plt.subplots(figsize=(6, 5))
    sns.countplot(data=filtered_df, x="change", hue="readmitted", palette="Set2", ax=ax7)
    ax7.set_title("Medication Change vs Readmission")
    ax7.set_xlabel("Medication Change")
    ax7.set_ylabel("Count")
    st.pyplot(fig7)
st.info("""
- Patients prescribed Insulin were less likely to be readmitted to hospital than those not prescribed it.
- Medication changes had little to no impact on readmission rates.
""")
st.markdown("---")
 

st.subheader("🖱️ Interactive: Age & A1C Result vs Readmittance")
st.info("Explore how age range and A1C result relate to readmission status. Each panel represents a different test result. Use the filters on the left to narrow down groups.")
age_a1c_df = filtered_df.groupby(["age", "A1Cresult", "readmitted"]).size().reset_index(name="count")
age_a1c_totals = age_a1c_df.groupby(["age", "A1Cresult"])["count"].transform("sum")
age_a1c_df["percentage"] = (age_a1c_df["count"] / age_a1c_totals * 100).round(1)
fig10 = px.bar(
    age_a1c_df,
    x="age",
    y="percentage",
    color="readmitted",
    facet_col="A1Cresult",
    labels={"age": "Age Range", "percentage": "Percentage (%)", "readmitted": "Readmitted", "A1Cresult": "A1C Result"},
    title="Age & A1C Result vs Readmittance (%)",
    category_orders={"age": age_ranges},
    barmode="group"
)
fig10.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig10, use_container_width=True)