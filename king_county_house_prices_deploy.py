# -*- coding: utf-8 -*-
"""King County House Prices Deploy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ODP911mLEgbpaGo6HPbQ2u3UeKYgPz91
"""

# !pip install streamlit

import streamlit as st
import pandas as pd
# from sklearn.preprocessing import  LabelEncoder
import xgboost as xgb
import numpy as np

st.header("House Price Prediction App (King County)")
# st.text_input("Enter your Name: ", key="name")
data = pd.read_csv("https://raw.githubusercontent.com/AimAndIgnite/datasets/main/kc_house_data.csv")

if st.checkbox('Show dataframe'):
    data
    
xgb_model = xgb.XGBRegressor()
xgb_model.load_model("model_sf.json")

st.subheader("Please select relevant features of your house:")

input_bathrooms = st.slider('Number of bathrooms', 0, max(data["bathrooms"]), 1)
input_bedrooms = st.slider('Number of bedrooms', 0, max(data["bedrooms"]), 1)
input_sqft_living = st.slider('Total living space (in square foot)', 0, max(data["sqft_living"]), 1)
input_sqft_above = st.slider('Total space (in square foot)', 0, max(data["sqft_above"]), 1)

if st.button('Make Prediction'):
    prediction = xgb_model.predict(input_bathrooms, input_bedrooms, input_sqft_living, input_sqft_above)
    print("final pred", np.squeeze(prediction, -1))
    st.write(f"Predicted clicks: {np.squeeze(prediction, -1)} clicks")
