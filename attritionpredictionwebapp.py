import streamlit as st

def set_bg_hack_url():    
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://img.freepik.com/free-vector/halftone-background-with-circles_23-2148907689.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack_url()

import numpy as np
import pickle

# Loading saved model and scalar
loaded_model = pickle.load(open('C:/Users/devik/OneDrive/Desktop/project_ml/trained_model.sav', 'rb'))
loaded_scalarmodel = pickle.load(open('C:/Users/devik/OneDrive/Desktop/project_ml/scalar.sav', 'rb'))

#streamlit run C:/Users/devik/OneDrive/Desktop/project_ml/attritionpredictionwebapp.py


# Label encoding
BusinessTravel = {'Travel_Rarely': 0, 'Travel_Frequently': 1, 'Non-Travel': 2}
Department = {'Human Resources': 0, 'Sales': 1, 'Research & Development': 2}
EducationField = {'Technical Degree': 0, 'Marketing': 1, 'Other': 2, 'Medical': 3, 'Human Resources': 4, 'Life Sciences': 5}

Gender = {'Male': 0, 'Female': 1}
JobRole = {'Research Director': 0, 'Sales Representative': 1, 'Research Scientist': 2, 'Manufacturing Director': 3,
           'Healthcare Representative': 4, 'Laboratory Technician': 5, 'Sales Executive': 6, 'Human Resources': 7,
           'Manager': 8}
MaritalStatus = {'Divorced': 0, 'Married': 1, 'Single': 2}
OverTime = {'Yes': 0, 'No': 1}

    
# Function to predict attrition
def attrition_Prediction(input_data):
    # Convert categorical variables to numerical using label encoding
    input_data[1] = BusinessTravel.get(input_data[1], -1)
    input_data[3] = Department.get(input_data[3], -1)
    input_data[6] = EducationField.get(input_data[6], -1)
    input_data[8] = Gender.get(input_data[8], -1)
    input_data[12] = JobRole.get(input_data[12], -1)
    input_data[14] = MaritalStatus.get(input_data[14], -1)
    input_data[18] = OverTime.get(input_data[18], -1)

    # Handle cases where the input data contains unknown categories
    if -1 in input_data:
        st.error("Please select valid options for categorical variables.")
        return

    # Convert input data to a numpy array
    input_data_array = np.asarray(input_data)

    # Reshape the array as we are predicting for one instance
    input_reshaped = input_data_array.reshape(1, -1)

    # Make predictions
    prediction = loaded_model.predict(input_reshaped)

    if prediction[0] == 0:
        return 'No Attrition'
    else:
        return 'Yes Attrition'

# Streamlit app for prediction page
def show_predict_page():
    st.title('Attrition Prediction')

    # Getting the input data from the users
    Age = st.text_input('Enter the age')
    BusinessTravel = st.selectbox('Business Travel', ('Travel_Rarely', 'Travel_Frequently', 'Non-Travel'),
                                  index=None, placeholder="Choose an option")
    DailyRate = st.text_input('Daily rate')
    Department = st.selectbox('Department', ('Human Resources', 'Sales', 'Research & Development'),
                              index=None, placeholder="Choose an option")
    DistanceFromHome = st.text_input('Distance from home')
    Education = st.text_input('Education')
    EducationField = st.selectbox('Education Field',
                                  ('Technical Degree', 'Marketing', 'Other', 'Medical', 'Human Resources', 'Life Sciences'),
                                  index=None, placeholder="Choose an option")
    EnvironmentSatisfaction = st.text_input('Environment satisfaction')
    Gender = st.selectbox('Gender', ('Male', 'Female'), index=None, placeholder="Choose an option")
    HourlyRate = st.text_input('Hourly Rate')
    JobInvolvement = st.text_input('Job involvement')
    JobLevel = st.text_input('Job level')
    JobRole = st.selectbox('Job role',
                           ('Research Director', 'Sales Representative', 'Research Scientist', 'Manufacturing Director',
                            'Healthcare Representative', 'Laboratory Technician', 'Sales Executive', 'Human Resources',
                            'Manager'), index=None, placeholder="Choose an option")
    JobSatisfaction = st.text_input('Job satisfaction')
    MaritalStatus = st.selectbox('Marital status', ('Divorced', 'Married', 'Single'), index=None,
                                 placeholder="Choose an option")
    MonthlyIncome = st.text_input('Monthly income')
    MonthlyRate = st.text_input('Monthly rate')
    NumCompaniesWorked = st.text_input('Number of companies worked')
    OverTime = st.selectbox('Overtime', ('Yes', 'No'), index=None, placeholder="Choose an option")
    PercentSalaryHike = st.text_input('Percentage of salary hike')
    PerformanceRating = st.text_input('Performance rating')
    RelationshipSatisfaction = st.text_input('Relationship satisfaction')
    StockOptionLevel = st.text_input('Stock option level')
    TotalWorkingYears = st.text_input('Total working years')
    TrainingTimesLastYear = st.text_input('Training time last year')
    WorkLifeBalance = st.text_input('Work life balance')
    YearsAtCompany = st.text_input('Years at company')
    YearsInCurrentRole = st.text_input('Years in current role')
    YearsSinceLastPromotion = st.text_input('Years since last promotion')
    YearsWithCurrManager = st.text_input('Years with current manager')

    # Code for prediction
    attrition_result = ''
    if st.button("Attrition Test Result"):
        attrition_result = attrition_Prediction(
            [Age, BusinessTravel, DailyRate, Department, DistanceFromHome, Education, EducationField,
             EnvironmentSatisfaction, Gender, HourlyRate, JobInvolvement, JobLevel, JobRole, JobSatisfaction,
             MaritalStatus, MonthlyIncome, MonthlyRate, NumCompaniesWorked, OverTime, PercentSalaryHike,
             PerformanceRating, RelationshipSatisfaction, StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear,
             WorkLifeBalance, YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager])

    st.success(attrition_result)

if __name__ == "__main__":

    show_predict_page()
