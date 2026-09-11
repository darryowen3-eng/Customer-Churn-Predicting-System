import streamlit as st

import requests



st.title("CUSTOMER CHURN PREDICTOR")
st.write("fill in, the information below to predict whether your customer will leave/not leave")


col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age of a customer", min_value=18, max_value=100)
    
    last_login = st.number_input("Number of days since they last logged in", min_value=0, value=5)

with col2:
    call = st.number_input("Number of calls recieved from customer about complaints", min_value=0, value=2)
    
    spenditure = st.number_input("Money spent by this customer per month", min_value=0, value=150)
    
    
if st.button("Click to predict", use_container_width=True):
    
    data = {
        "Age": int(age),
        "Days_Since_Last_Login": int(last_login),
        "Customer_Service_Calls": int(call),
        "Monthly_Spend": float(spenditure)
    }
    
    
    api_url = "https://customer-churn-predictor-api-sjri.onrender.com/predict"
    
    response = requests.post(api_url, json=data, timeout=60)
    
    try:
        
        with st.spinner("Please wait as we analize data......"):
            results = response.json()
    
        if response.status_code==200:
            
            prediction=results.get("prediction")
            probability=results.get("probability")
            
            shap_values = results.get("shap_values", [])
            
            status_mapping = {0:"The customer will not leave", 1:"The customer will leave"}
            final_status = status_mapping.get(prediction, "unknown")
            
            if prediction==0:
                st.success(f"Churn Status: {final_status}")
            
            elif prediction==1:
                st.success(f"Churn Status: {final_status}")
                
            else:
                st.error(f"Error: {final_status}")
            
            st.subheader("-----Model Confidence Metrics-----")
    
            st.write(f"Model Confidence Score: {probability:.2%}")
            
            if shap_values and len(shap_values) == 4:
                st.subheader("----- Why did the model decide this? -----")
                st.write("Here are the factors that influenced this decision, ordered by impact:")
                
                
                feature_labels = [
                    "Age of customer", 
                    "Days since last login", 
                    "Customer service calls", 
                    "Monthly spend"
                     ]
                
                input_values = [age, last_login, call, spenditure]
                
                explanation_data = list(zip(feature_labels, input_values, shap_values))
                
                sorted_explanations = sorted(explanation_data, key=lambda x: abs(x[2]), reverse=True)
                
                
                for feature, val, score in sorted_explanations:
                    if score > 0:
                        direction = "🔴 increases the likelihood of leaving"
                    else:
                        direction = "🟢 reduces the likelihood of leaving"
                
                    st.write(f"- **{feature}** (`{val}`): This {direction} (Impact score: {score:+.3f})")
        
            
        else:
            st.error(f"Error: {response.status_code}")
            
            
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the API server. Check if your backend container is running properly.")
