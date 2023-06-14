import streamlit as st
import pickle
import numpy as np

# setting the page configuration 
st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻", layout="wide")
st.title("Laptop Price Predictor 💻")

# importing the model and the pickle dataset 
df = pickle.load(open("dataset.pkl", "rb"))
pipe = pickle.load(open("model.pkl", "rb"))

headings = ['Brand', 'Processor Brand', 'Processor Model', 'Generation', 'Processor Core', 'Processor Thread', 'CPU Cache', 'RAM', 'RAM Type', 'Storage Capacity', 'Display Size', 'Graphics Memory', 'Battery Capacity']
heading_map = dict(zip(headings, ["NULL"] * len(headings)))
max_len = len(headings)

ind = 0
for row in range(0, 5):
    if ind == max_len:
        break
    taken = st.columns(4)
    
    for col in range(0, 3):
        if ind == max_len:
            break

        with taken[col]:
            # storing the results in the heading_map
            heading_map[headings[ind]] = st.selectbox(headings[ind], df[headings[ind]].unique())
            ind += 1

# collecting the user input from the map 
user_input = []
for data in range(len(heading_map)):
    user_input.append(heading_map[headings[data]])

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
    # st.image('Images\laptop.jpg',width=600)
#     st.text("Sir/Maam,YOU need to fill all the neccesary informations in order to know the price!")

    # st.sidebar.multiselect('choose a Brand', ['ASUS', 'Dell', 'HP', 'Apple'])
#     st.sidebar.multiselect('choose RAM',['8GB', '16GB', '32GB','64GB'])
#     st.sidebar.multiselect('choose Processor',['Intel', 'AMD'])
#     st.sidebar.multiselect('choose Processor Core ',['Core i3', 'Core i5', 'Core i7'])
#     st.button("Predict")

# predict the price only if the button is pressed
if st.button("Predict Price"):

    # passing the user input as queries 
    query = np.array(user_input)
    query = query.reshape(1, 13)

    st.title("The Predicted Price of Laptop = Rs " + str(int(np.exp(pipe.predict(query)[0]))))
