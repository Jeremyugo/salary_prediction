import pandas as pd
import numpy as np
import streamlit as st
from sk_class import DataFrameSelector
from PIL import Image
from joblib import load

data = load('C://Users//jeremiah.chinyelugo.HEOSL//Desktop//salary_prediction.txt')


st.title("Salary Prediction")
img = Image.open('C://Users//jeremiah.chinyelugo.HEOSL//Desktop//salary.jpeg')
st.image(img)

expander = st.sidebar.beta_expander("Assumptions used when training the Data")
expander.write("""   * CEO'S, CFO'S, CTO'S & VICE PRESIDENT'S should have at least a bachelor's degree
               
   * CEO'S, CFO'S, CTO'S & VICE PRESIDENT'S should have at least 10 years experience even with a bachelor's degree
   
   * CEO'S, CFO'S, CTO'S & VICE PRESIDENT'S should have at least 5 years experience even with an advanced degree
   
   
   * MANAGER'S & SENIOR'S should have at least a bachelor's degree
   
   * MANAGER'S & SENIOR'S should have at least 5 years experience even with a bachelor's degree
   
   * MANAGER'S & SENIOR'S should have at least 3 years experience even with an advanced degree
   
   * JANITORS have at most, a high school degree and no major""")
    
st.write("### We need some information to predict you Salary")
    
    
titles = ("JANITOR","JUNIOR","SENIOR","MANAGER","VICE_PRESIDENT",
        "CTO","CFO","CEO")
    
    
title = st.selectbox("Job Title", titles)

if title == 'JANITOR':
    degree = st.selectbox("Degree", ("NONE","HIGH_SCHOOL"))
    major = st.selectbox("Major", ["NONE"])
    industry = st.selectbox("Industry", ('AUTO', 'EDUCATION', 'SERVICE', 'HEALTH', 'WEB', 'FINANCE', 'OIL'))
    experience = st.slider("Experience (years)", 0, 24)
    miles = st.slider("Distance of Job Location from Nearest Major City", 0, 99)
    
elif title == 'JUNIOR':
    degree = st.selectbox("Degree", ("NONE","HIGH_SCHOOL", "BACHELORS", "MASTERS", "DOCTORAL"))
    if degree in ["NONE","HIGH_SCHOOL"]:
        major = st.selectbox("Major", ["NONE"])
        industry = st.selectbox("Industry", ('AUTO', 'EDUCATION', 'SERVICE', 'HEALTH', 'WEB', 'FINANCE', 'OIL'))
        experience = st.slider("Experience (years)", 0, 24)
        miles = st.slider("Distance of Job Location from Nearest Major City", 0, 99)
    elif degree in ["BACHELORS", "MASTERS", "DOCTORAL"]:
        major = st.selectbox("Major", ('LITERATURE', 'CHEMISTRY', 'PHYSICS', 'BIOLOGY', 'COMPSCI',
          'ENGINEERING', 'BUSINESS', 'MATH'))
        industry = st.selectbox("Industry", ('AUTO', 'EDUCATION', 'SERVICE', 'HEALTH', 'WEB', 'FINANCE', 'OIL'))
        experience = st.slider("Experience (years)", 0, 24)
        miles = st.slider("Distance of Job Location from Nearest Major City", 0, 99)
    
    
    
elif title in ['SENIOR','MANAGER']:
    degree = st.selectbox("Degree", ("BACHELORS", "MASTERS", "DOCTORAL"))
    if degree == 'BACHELORS':
        major = st.selectbox("Major", ('LITERATURE', 'CHEMISTRY', 'PHYSICS', 'BIOLOGY', 'COMPSCI',
          'ENGINEERING', 'BUSINESS', 'MATH'))
        industry = st.selectbox("Industry", ('AUTO', 'EDUCATION', 'SERVICE', 'HEALTH', 'WEB', 'FINANCE', 'OIL'))
        experience = st.slider("Experience (years)", 5, 24)
        miles = st.slider("Distance of Job Location from Nearest Major City", 0, 99)
    elif degree in ["MASTERS", "DOCTORAL"]:
        major = st.selectbox("Major", ('LITERATURE', 'CHEMISTRY', 'PHYSICS', 'BIOLOGY', 'COMPSCI',
          'ENGINEERING', 'BUSINESS', 'MATH'))
        industry = st.selectbox("Industry", ('AUTO', 'EDUCATION', 'SERVICE', 'HEALTH', 'WEB', 'FINANCE', 'OIL'))
        experience = st.slider("Experience (years)", 3, 24)
        miles = st.slider("Distance of Job Location from Nearest Major City", 0, 99)
        
elif title in ['VICE_PRESIDENT','CFO', 'CEO', 'CTO']:
    degree = st.selectbox("Degree", ("BACHELORS", "MASTERS", "DOCTORAL"))
    if degree == 'BACHELORS':
        major = st.selectbox("Major", ('LITERATURE', 'CHEMISTRY', 'PHYSICS', 'BIOLOGY', 'COMPSCI',
          'ENGINEERING', 'BUSINESS', 'MATH'))
        industry = st.selectbox("Industry", ('AUTO', 'EDUCATION', 'SERVICE', 'HEALTH', 'WEB', 'FINANCE', 'OIL'))
        experience = st.slider("Experience (years)", 10, 24)
        miles = st.slider("Distance of Job Location from Nearest Major City", 0, 99)
    elif degree in ["MASTERS", "DOCTORAL"]:
        major = st.selectbox("Major", ('LITERATURE', 'CHEMISTRY', 'PHYSICS', 'BIOLOGY', 'COMPSCI',
          'ENGINEERING', 'BUSINESS', 'MATH'))
        industry = st.selectbox("Industry", ('AUTO', 'EDUCATION', 'SERVICE', 'HEALTH', 'WEB', 'FINANCE', 'OIL'))
        experience = st.slider("Experience (years)", 5, 24)
        miles = st.slider("Distance of Job Location from Nearest Major City", 0, 99)


ok = st.button("Predict Salary")
if ok:
    X = pd.DataFrame(np.array([[title, degree, major, industry, experience, miles]], dtype=object),
                 columns = ['jobType', 'degree', 'major', 'industry', 'yearsExperience','milesFromMetropolis'])
    
    salary = data.predict(X)
    st.subheader(f"The Estimated Salary is ${(salary[0])*1000:,.0f}")
    
    
    



    