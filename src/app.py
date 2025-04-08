import streamlit as st
import pandas as pd
import pickle

# Load model
with open("C:/Users/shaan/Autism_Predictor_App/Models/best_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Autism Spectrum Disorder Predictor")
st.markdown("### Please answer the questions below")

# Form input
with st.form("autism_form"):
    A1 = st.selectbox("A1: Notices small sounds others don’t?", [0, 1])
    A2 = st.selectbox("A2: Focuses on small details more than the big picture?", [0, 1])
    A3 = st.selectbox("A3: Can do more than one thing at once?", [0, 1])
    A4 = st.selectbox("A4: Finds it easy to switch between activities?", [0, 1])
    A5 = st.selectbox("A5: Finds imaginative play difficult?", [0, 1])
    A6 = st.selectbox("A6: Enjoys social occasions?", [0, 1])
    A7 = st.selectbox("A7: Easily notices patterns in things?", [0, 1])
    A8 = st.selectbox("A8: Not good at interpreting others’ feelings?", [0, 1])
    A9 = st.selectbox("A9: Enjoys small talk?", [0, 1])
    A10 = st.selectbox("A10: Prefers doing things the same way every time?", [0, 1])

    age = st.number_input("Age", min_value=1, max_value=100, value=25)
    gender = st.selectbox("Gender", ["Male", "Female"])
    jaundice = st.selectbox("Has the person had jaundice?", ["Yes", "No"])
    family_mem_with_ASD = st.selectbox("Any family member with Autism?", ["Yes", "No"])
    ethnicity = st.selectbox("Ethnicity", ["White-European", "Latino", "Black", "Asian", "Others"])
    country_of_res = st.selectbox("Country of residence", ["United States", "India", "United Kingdom", "Others"])
    used_app_before = st.selectbox("Used this screening app before?", ["Yes", "No"])
    relation = st.selectbox("Who is filling this form?", ["Self", "Parent", "Health Care Professional", "Others"])

    # Compute 'result' if it’s a sum of A1-A10 scores (adjust based on dataset)
    result = A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10

    submit = st.form_submit_button("Predict")

if submit:
    # Prepare input
    input_dict = {
        "A1_Score": A1, "A2_Score": A2, "A3_Score": A3, "A4_Score": A4, "A5_Score": A5,
        "A6_Score": A6, "A7_Score": A7, "A8_Score": A8, "A9_Score": A9, "A10_Score": A10,
        "age": age, "gender": gender, "ethnicity": ethnicity, "jaundice": jaundice,
        "austim": family_mem_with_ASD, "contry_of_res": country_of_res, 
        "used_app_before": used_app_before, "result": result, "age_desc": "18 and more", 
        "relation": relation
    }

    df = pd.DataFrame([input_dict])
    df = pd.get_dummies(df, columns=['gender', 'ethnicity', 'jaundice', 'austim', 
                                     'contry_of_res', 'used_app_before', 'age_desc', 'relation'])

    # Align with model features
    for col in model.feature_names_in_:
        if col not in df.columns:
            df[col] = 0
    df = df[model.feature_names_in_]

    # Predict
    probability = model.predict_proba(df)[0][1]
    threshold = 0.4  # Adjust based on desired sensitivity

    if probability >= threshold:
        st.error(f"⚠️ High chance of Autism (Probability: {probability:.2%})")
    else:
        st.success(f"✅ Low chance of Autism (Probability: {probability:.2%})")