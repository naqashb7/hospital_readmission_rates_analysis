import streamlit as st

st.title("⚖️ Ethical Considerations")
st.markdown("""
## Ethics Overview
AI and data ethics is a set of principles and guidelines ensuring artificial intelligence and data usage are fair, transparent, accountable, and secure,
aiming to prevent harm and uphold human rights. It addresses ethical risks like bias, privacy violations, and misuse of technology, ensuring technologies are developed 
and deployed responsibly. 
            
---
            
# GDPR

The General Data Protection Regulation (GDPR) is a comprehensive European Union law enacted on May 25, 2018, that governs how organizations collect, use, store, and protect the personal data of individuals within the EU. 
It focuses on privacy rights, transparency, and data accountability, giving individuals greater control over their personal information.
            

---

## Bias
            
* Automation Bias – The data is US data and from the original analysis and visualisations, indicate that 4 days was the mean stay length for patients who were readmitted to hospital. In the US, healthcare works via an insurance system. 
            It may be that the longer stays required longer care, however, patients may not have been able to afford the care which led to discharge. 
            Early discharge may cause patients to not receive full care and hence cause patients to return to hospital. 
            This indicates health inequalities within the economic system, something that is not considered by my model as it is not a feature of the dataset. 
            Automation bias needs to be considered here as an ethical issue as over reliance on the model could lead to ignorance around other factors impacting readmittance. 
* Algorithmic Bias – Algorithmic bias is bias in the model due to human prejudices often caused by skewed, unrepresentative or flawed data. 
            The use of age, gender and race from this dataset can cause algorithmic bias as the data may have been flawed. 
            The model will then create its own assumptions and understanding from that data creating a bias.
* Historic data – This data is historical data from between 1999-2008. This means that the data is almost outdated by 20 years.
            There has been a lot of medical and economic evolution since then. 
            The outcomes from this data and the predictive analytics of the model may not be relevant today as the clinical practices and economic structures will have changed since then.


---
            
## Privacy & GDPR
Data minimisation is a core privacy principle within GDPR requirements. 
The US does not have a similar framework and so this data does not follow those requirements. 
To follow those requirements, the following columns were removed and were identified as either sensitive health, economic or unique identifiable information:

* Weight – sensitive health data. <mark style='background-color: #FF6B6B; color: white;'>*REMOVED*</mark>
* Payer code – sensitive health and economic information <mark style='background-color: #FF6B6B; color: white;'>*REMOVED*</mark>
* Encounter ID – sensitive identifiable information <mark style='background-color: #FF6B6B; color: white;'>*REMOVED*</mark>
* Patient Number - sensitive identifiable information <mark style='background-color: #FF6B6B; color: white;'>*REMOVED*</mark>
* Admission Type ID - sensitive identifiable information <mark style='background-color: #FF6B6B; color: white;'>*REMOVED*</mark>
* Admission Source ID - sensitive identifiable information <mark style='background-color: #FF6B6B; color: white;'>*REMOVED*</mark>

This allows me to still be able to build an effective predictive model while reducing the risk of patients being identified from the data.



---            
## Fairness & Social Impact
            


In the data, some records show that some patients had more visits than others. 
This initially indicates that patients needed to keep coming back to hospital for more treatment. 
In reality, this may not have been the case as it may have been that the patients did not have access to the adequate healthcare for their treatment in the first place. 
This should be further investigated, especially as the data is from across 130 different US hospitals and so the quality of healthcare would not necessarily have been universal. 

            
The dataset indicates that African American patients had to be readmitted more often than any of the other ethnicities. 
Based off of this model, it would indicate that race was likely to cause readmittance. 
However, in reality, it could be that health inequality was the actual cause and in more dense African American areas, lower quality healthcare was leading to readmittance of patients. 
The aim with AI should be that outcomes lead to a fair solution and is not more beneficial to one group of people over another. This is why fairness is important to considered.
        
            
            
""", unsafe_allow_html=True)