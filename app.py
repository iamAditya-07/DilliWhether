import streamlit as st
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('model.pkl', 'rb'))
data = pickle.load(open('data.pkl', 'rb'))

st.title("Delhi Transport")

dew = st.number_input("Enter dewpoint value")

hail = st.selectbox("Hailstorms?",['Yes','No'])

h_index = st.slider("Select Heatindex value",0,70,0)

pressure = st.slider("Select pressure value",-9999,10000,0)

rain = st.selectbox("Is it raining?",['Yes', 'No'])

snow = st.selectbox("Is it snowfalling",['Yes', 'No'])

thunder = st.selectbox("Thunderous weather?",['Yes', 'No'])

tornado = st.selectbox("Any signs of tornado?",['Yes', 'No'])

vis = st.slider("Select visibility range (in miles)",0,10,0)

wdir = st.number_input("Enter wind direction value (in degrees)")

wgust = st.slider("Select windgust value(mph)",0,90,0)

wchill = st.slider("Select windchill value (mph)",0,7,0)

wspeed = st.slider("Select windspeed value (mph)",0,200,0)

if st.button('Suggest Vehicle'):

    if hail=='Yes':
        hail = 1
    else:
        hail = 0

    if rain=='Yes':
        rain = 1
    else:
        rain = 0

    if snow=='Yes':
        snow = 1
    else:
        snow = 0

    if thunder=='Yes':
        thunder = 1
    else:
        thunder = 0

    if tornado=='Yes':
        tornado = 1
    else:
        tornado = 0

    
    query = np.array([dew, hail, h_index, pressure, rain, snow, thunder, tornado, vis, wdir, wgust, wchill, wspeed])
    query = query.reshape(1,13)
    x = model.predict(query)
    if x[0]==1:
        st.title('You should prefer *CYCLE*')
    elif x[0]==1:
        st.title('You should prefer *CAR* or *BIKE*')
    else:
        st.title('You should prefer *METRO*')





