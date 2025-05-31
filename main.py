import streamlit as st
from prediction_helper import predict

# Define the page layout
st.set_page_config(page_title="Health Rate", layout="wide")  # Set app title and layout
st.title('Health Premium Estimator')

# Adding a subheader
st.subheader("Predict your health insurance costs based on various factors.")

# Categorical options for the input fields
categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# Create four rows of three columns each
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# Assign inputs to the grid
with row1[0]:
    age = st.number_input('Age', min_value=18, step=1, max_value=100)
with row1[1]:
    number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20)
with row1[2]:
    income_lakhs = st.number_input('Income in Lakhs', step=1, min_value=0, max_value=200)

with row2[0]:
    genetical_risk = st.number_input('Genetical Risk', step=1, min_value=0, max_value=5)
with row2[1]:
    insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])
with row2[2]:
    employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])

with row3[0]:
    gender = st.selectbox('Gender', categorical_options['Gender'])
with row3[1]:
    marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
with row3[2]:
    bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])

with row4[0]:
    smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
with row4[1]:
    region = st.selectbox('Region', categorical_options['Region'])
with row4[2]:
    medical_history = st.selectbox('Medical History', categorical_options['Medical History'])

# Create a dictionary for input values entered by the user.
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# Button to make prediction
if st.button('Predict'):
    prediction = predict(input_dict)
    st.success(f'Predicted Health Insurance Cost: ₹{prediction}')


# Add a custom hamburger icon to replace the current header button
st.markdown("""
<style>
/* Target the header button using its data-testid */
[data-testid="baseButton-headerNoPadding"] {
    background: none; /* Remove default background */
    border: none; /* Remove border */
    cursor: pointer; /* Change cursor to pointer */
}

/* Replace the SVG with a hamburger icon */
[data-testid="baseButton-headerNoPadding"] svg {
    display: none; /* Hide the default SVG */
}

[data-testid="baseButton-headerNoPadding"]::before {
    content: '\\2630'; /* Unicode for hamburger icon */
    font-size: 24px; /* Adjust icon size */
    color: currentColor; /* Inherit color for consistency */
    display: block;
}
</style>
""", unsafe_allow_html=True)


# Add footer with professional details
st.markdown("---")
st.markdown("""
<div style='text-align: center;'>
    <h4>A Project by ~ Adin Raja ✌️</h4>
    <p>
        <a href='https://github.com/adin11' target='_blank'>GitHub</a> | 
        <a href='https://www.linkedin.com/in/adin-raja-492a78194/' target='_blank'>LinkedIn</a> | 
        <a href='mailto:adinraja78@gmail.com'>Email</a>
    </p>
    <small>© 2024 Adin Raja. All rights reserved.</small>
</div>
""", unsafe_allow_html=True)

# Optional Sidebar for About Section
with st.sidebar:
    
    with st.sidebar:
     st.markdown("### 🏥 About This App")  # Changed the icon to a hospital symbol

    st.info(
        """
        This is a **Health Insurance Cost Predictor** app. Enter your details to get a prediction of 
        your health insurance costs. \n
        **Made by ~ Adin**
        """
    )
    st.markdown("### 📬 Contact")  # Updated the icon to an envelope symbol
    st.write("""
    - ✉️ Email: [adinraja78@gmail.com](mailto:your_email@example.com)
    - 💼 [LinkedIn](https://www.linkedin.com/in/adin-raja-492a78194/)
    - 🖥️ [GitHub](https://github.com/adin11)
    """)
















