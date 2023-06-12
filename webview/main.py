import streamlit as st
import pickle
import numpy as np

# importing the model and the pickle dataset 
df = pickle.load(open("dataset.pkl", "rb"))

left_column, middle_column, right_column, corner_column = st.columns(4)
with left_column:
    # laptop brand
    laptop_brand = st.selectbox("Brand", df["Brand"].unique())

with middle_column:
    # processor brand
    pro_brand = st.selectbox("Processor Brand", df["Processor Brand"].unique())

with right_column:
    # Ram size
    ram = st.selectbox("Processor Model", df["Processor Model"].unique())

# st.sidebar.title("Welcome to LapTopPricePredix")
# @st.cache(suppress_st_warning=True)
# def get_fvalue(val):
#     feature_dict = {"No": 1, "Yes": 2}
#     for key, value in feature_dict.items():
#         if val == key:
#             return value

# def get_value(val, my_dict):
#     for key, value in my_dict.items():
#         if val == key:
#             return value

# app_mode = st.sidebar.selectbox('Select Page', ['Home', 'Prediction'])  # two pages

# if app_mode=='Home':    
#     st.title('Laptop Price PREDICTION :') 
#     st.image('Images\laptop.jpg',width=600)

# elif app_mode == 'Prediction':
#     st.image('Images\laptop.jpg',width=600)
#     st.text("Sir/Maam,YOU need to fill all the neccesary informations in order to know the price!")

    # st.sidebar.multiselect('choose a Brand', ['ASUS', 'Dell', 'HP', 'Apple'])
#     st.sidebar.multiselect('choose RAM',['8GB', '16GB', '32GB','64GB'])
#     st.sidebar.multiselect('choose Processor',['Intel', 'AMD'])
#     st.sidebar.multiselect('choose Processor Core ',['Core i3', 'Core i5', 'Core i7'])
#     st.button("Predict")