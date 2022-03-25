import streamlit as st
import tensorflow as tf
from PIL import Image
import pickle
import numpy as np
import pandas as pd
import requests


def predict_weather(location,begintime,endtime):

    data ={
    "LOCATION": location,
    "BEGIN TIME": begintime,
    "END TIME": endtime
    }
    response = requests.post('http://127.0.0.1:8000/predict',json=data)
    return response
    


def main():
    st.title("STORM PREDICTION FOR FARMERS")
    html_temp = """
    <div style="background-color:green;text-align:center;padding:15px">
    <h3 style="color:white;text-align:center;">This app shows storm prediction for farmers </h3>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    location = st.text_input("LOCATION")
    begintime = st.text_input("BEGIN Time")
    endtime = st.text_input("END TIME")
    result=""
    if st.button("Predict"):
        #result=
        img = predict_weather(location,begintime,endtime)
    st.success('The output is {}'.format(result))
    st.image(img.content)
    if st.button("About"):
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()