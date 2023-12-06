#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import streamlit as st 
import warnings
warnings.filterwarnings('ignore')
import os


# In[26]:
os.chdir(r"C:\Users\Renu\Downloads\P302\deployment")
st.title(":blue[Project 302: World development data]")
st.sidebar.header('User Input Parameters')

def user_input_features():
    Birth_Rate = st.sidebar.number_input("Birth Rate: between 0.007 and 0.053 ")
    CO2_Emissions = st.sidebar.number_input('co2 emission: value 7million to 8.3 million')
    GDP = st.sidebar.number_input("GDP:63.1m to 16 trillion")
    Health_Exp_GDP = st.sidebar.number_input('Health Exp GDP % :value 0.008 to 0.225')
    Health_Exp_Capita = st.sidebar.number_input('Health Exp/Capita: value 2 to 9908')
    Infant_Mortality_Rate = st.sidebar.number_input('Infant Mortality Rate: value 0.002 to 0.141')
    Internet_Usage = st.sidebar.number_input('Internet Usage; value 0 to 1')
    Mobile_Usage = st.sidebar.number_input('Mobile Phone Usage:value 0 to 2.9')
    Population_Total = st.sidebar.number_input('Population Total:value 18876 to 1 billion')
    Population_Urban = st.sidebar.number_input('Population Urban: value 0.082 to 1')
    Tourism_Inbound= st.sidebar.number_input('Tourism Inbound: value 700,000 to 200 billions')
    Tourism_Outbound = st.sidebar.number_input('Tourism Outbound: 200,000 to 126 billions')
    life_expectancy = st.sidebar.number_input('life expectancy: value 37 to 88')



    data = {'Birth Rate':Birth_Rate,'CO2 Emissions':CO2_Emissions,'GDP':GDP,'Health Exp GDP':Health_Exp_GDP, 
            'Health Exp Capita':Health_Exp_Capita,'Infant Mortality Rate':Infant_Mortality_Rate,
            'Internet Usage':Internet_Usage,'Mobile Phone Usage': Mobile_Usage,
            'Population Total':Population_Total,'Population Urban':Population_Urban,
            'Tourism Inbound':Tourism_Inbound,'Tourism Outbound':Tourism_Outbound,'life_expectancy':life_expectancy}

    
    features = pd.DataFrame(data,index = [0])
    return features 


# In[27]:


df_in = user_input_features()
st.subheader('Input parameters')
st.write(df_in)


st.subheader('Prediction')

import pickle
if df_in.values[0].sum()==0:
    st.write(":orange[Inputs not given]")
else:   
    model = pickle.load(open('models\model.pkl','rb'))
    prediction = model.predict(df_in)
    st.write(prediction)



# In[ ]:




