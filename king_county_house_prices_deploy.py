# -*- coding: utf-8 -*-
"""King County House Prices Deploy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ODP911mLEgbpaGo6HPbQ2u3UeKYgPz91
"""

# !pip install streamlit

import streamlit as st
import pandas as pd
from sklearn.preprocessing import  LabelEncoder
import xgboost as xgb
import numpy as np

st.header("Fish Weight Prediction App")
st.text_input("Enter your Name: ", key="name")
data = pd.read_csv("https://raw.githubusercontent.com/AimAndIgnite/datasets/main/kc_house_data.csv")

if st.checkbox('Show dataframe'):
    data
