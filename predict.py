from keras_preprocessing.image import img_to_array, load_img
from keras.models import load_model
import numpy as np
import streamlit as st
import os
from dal import *
from localPath import *
from login import *
import datetime 

model = load_model(modelpath)

@st.cache
def predict(img):
    imgpath = img
    img = load_img(imgpath, target_size=(64,64,3))
    img_array = img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_batch)
    prediction = labels[np.argmax(prediction)].get('name')
    os.remove(imgpath)
    return prediction

def show_prediction_page():
    st.title("Genkendelse af Simpsons karakterer")
    st.subheader("Forudsigelse af hvilken karakter som er på billedet")

    uploaded_file = st.file_uploader("Upload et billed", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Billedet du har uploadet")
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())
        prediction = predict(uploaded_file.name)
        st.success("Dette er et billed af : {}".format(prediction))
    else:
        st.info("Upload et billede")

    
    if uploaded_file is not None:
        st.write("Er det rigtigt? Klik på knappen nedenfor")

        col1, col2 = st.columns([1,1])

        with col1:
            sandt = st.button("Sandt")
        with col2:
            falsk = st.button("Falsk")

        if sandt:
            add_to_database(uploaded_file.name, prediction, author, datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
            st.success("Din forudsigelse er gemt") 
            st.balloons()
        if falsk:
            st.warning("Prøv igen")


    
