# Diabetic Patient Hospital Readmission App

**Diabetic Patient Hospital Readmission App** is an application to help understand the likelihood of a diabetes patient being readmitted to hospital based off a variety of clinical and demographic factors when entered into the app.[Click here to visit the app!](https://hospital-readmission-app-94c47532d5b0.herokuapp.com//)

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


## Dataset Content
* The dataset selected was a dataset from Kaggle that looked at data from 130 US hospitals during the period of 1999-2008. (https://www.kaggle.com/datasets/brandao/diabetes)
* Each record in the dataset represented a visit to hospital by the patient.
* The dataset was selected as it had a large variety of features to analyse that could impact patient readmission rates.
* The dataset contained the following information:
    * Encounter Id 
    * Patient Number
    * Gender 
    * Age
    * Race
    * Information on Diagnoses
    * Information on Blood testing
    * Readmittance - a column to show if the patient was readmitted to hospital after their encounter.
* The dataset is related to real-world issues as diabetes is a very common disease that affects many people worldwide. It is important to understand factors that can cause readmission as readmission in diabetes patients can have large costs to healthcare institutions.
* The dataset also had about 100,000 records which allowed for deriving meaningful conclusions and being able to understand the impact of different variables on patient readmission.

## Business Requirements
Business requirements were as follows:

* Identify what factors will increase the likelihood of diabetes patient readmittance to hospital.


## Hypotheses & Conclusions

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

## Project Plan
* The steps taken for analysis were as follows:
    1) ETL pipeline - Clean the raw data and export it to a clean data file
    2) EDA - visualise the data to determine patterns and connections
    3) Modelling - Create a new Model dataset and then use a Machine Learning model to predict patient readmission
    4) App - Build Streamlit App and deploy with predictive model
    5) Ethics - Document Ethical Considerations in app
* A breakdown of the tasks undertaken for the project can be seen [here](https://github.com/users/naqashb7/projects/3)


## Analysis techniques used
* Data visualisation using Heat maps, Count plots, Bar charts and Correlation Matrices were used to analyse the clean data.
* The Data was split between analysis of Numerical data and then Categorical data. It seemed like the natural split when analysing the data.
* The dataset was large but not of good quality. This limited me in achieving accurate conclusions from the data (even though it was real-world data). It also impacted the ML model and its predictive capabilities. In fact, the dataset was so poor that, the 2 ML models, when trained and tested, still could not accurately predict patient readmission records.
* There was a lot of information that was not needed and better data that should have been collected. This would have helped create more accurate models.
* I used Claude AI to help with code debugging and project structure planning.

## Ethical considerations
* The ethical considerations for this project were as follows:
    * Bias:
        * Automation Bias -The data is US data and from the original analysis and visualisations, indicate that 4 days was the mean stay length for patients who were readmitted to hospital. In the US, healthcare works via an insurance system. It may be that the longer stays required longer care, however, patients may not have been able to afford the care which led to discharge. Early discharge may cause patients to not receive full care and hence cause patients to return to hospital. This indicates health inequalities within the economic system, something that is not considered by my model as it is not a feature of the dataset. Automation bias needs to be considered here as an ethical issue as over reliance on the model could lead to ignorance around other factors impacting readmittance. 
        * Algorithmic Bias - Algorithmic bias is bias in the model due to human prejudices often caused by skewed, unrepresentative or flawed data. The use of age, gender and race from this dataset can cause algorithmic bias as the data may have been flawed. The model will then create its own assumptions and understanding from that data creating a bias.
        * Historic Data - This data is historical data from between 1999-2008. This means that the data is almost outdated by 20 years. There has been a lot of medical and economic evolution since then. The outcomes from this data and the predictive analytics of the model may not be relevant today as the clinical practices and economic structures will have changed since then.
    * Privacy & GDPR:
        * Data minimisation is a core privacy principle within GDPR requirements. The US does not have a similar framework and so this data does not follow those requirements. To follow those requirements, the following columns were removed and were identified as either sensitive health, economic or unique identifiable information:
            * Weight – sensitive health data. **REMOVED**
            * Payer code – sensitive health and economic information. **REMOVED**
            * Encounter ID – sensitive identifiable information. **REMOVED**
            * Patient Number - sensitive identifiable information. **REMOVED**
            * Admission Type ID - sensitive identifiable information. **REMOVED**
            * Admission Source ID - sensitive identifiable information. **REMOVED**
        * This allows me to still be able to build an effective predictive model while reducing the risk of patients being identified from the data.
    * Fairness & Social Impact:
        * In the data, some records show that some patients had more visits than others. This initially indicates that patients needed to keep coming back to hospital for more treatment. In reality, this may not have been the case as it may have been that the patients did not have access to the adequate healthcare for their treatment in the first place. This should be further investigated, especially as the data is from across 130 different US hospitals and so the quality of healthcare would not necessarily have been universal. 
        * The dataset indicates that African American patients had to be readmitted more often than any of the other ethnicities. Based off of this model, it would indicate that race was likely to cause readmittance. However, in reality, it could be that health inequality was the actual cause and in more dense African American areas, lower quality healthcare was leading to readmittance of patients. The aim with AI should be that outcomes lead to a fair solution and is not more beneficial to one group of people over another. This is why fairness is important to considered.
 

## Dashboard Design
* The Dashboard was built as a Streamlit App and was structured as follows:
    1) Introduction - A summary of the project as a whole
    2) Dataset - A snapshot of the dataset
    3) Visualisations - Visualisations derived from the dataset
    4) ML Model - A summary of the model selection process
    5) Predictor - A page to help predict pateint readmittance based off user inputs
    6) Ethical Considerations - A page to discuss AI and Data Ethics related to the project
* The dashboard caters for both Technical and Non-technical audiences because:
    * Technical Audiences can understand the model selection criteria
    * Non-technical audiences can understand the data used and the visualisations while also being able to use the prediction section
    * Both Technical and Non-technical audiences can understand the ethical considerations around the project.


## Development Roadmap & Reflection
* The ML pipeline was easier to do however, I would prefer more work to be done on the ETL of the data, maybe with more features.
* I tried to set up a neural network for predictive analytics however, there was a clash with tensorflow and the version of streamlit being run. Going forward I would definitely try this agin.
* Going forward I think I will look to other sources for data other than Kaggle. I have used Kaggle for my previous 3 projects and I appreciate it a lot but I think I want to practice more with other public data e.g. FCA, NHS, World Bank etc. and also potentially using web-scraping or API's
* This Dataset was large but I don't think the data quality was the best. It shows that both Data size and Data quality are essential for building effective models.
* Similarily to the previous project, in the future I would play around with model hyperparameters to better train the model and see which hyperparameters have a stronger impact on the model performance.

## Deployment
### Heroku

* Heroku was used to deploy the app.
* Initially there was an issue and the app wouldn't deploy.
* It was determined that the app path had to be defined in the Procfile and then redeployed.


## Main Data Analysis Libraries

The following Python libraries were used, alongside which section of the project they were utilised in:

* Pandas - ETL, EDA, Modelling, App
* Matplotlib - EDA, App
* Seaborn - EDA, App
* Plotly - App
* Scipy - Modelling
* Scikitlearn - Modelling, App
* Imbalanced Learn - Modelling
* Streamlit - App


## Credits 

* Kaggle for the dataset
* Code Institute for providing me with the opportunity to learn and become a proficient Data & AI practitioner
* Specifically Vasi, Mark & Neil for helping with the learning and the course as a whole
