from keras.preprocessing.image import img_to_array, load_img
from keras.models import load_model
import numpy as np
import pandas as pd
import streamlit as st
import os
from dal import *
from localPath import *

model = load_model(modelpath)

@st.cache
def predict(img):
    imgpath = samplepath+img
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
        with open(samplepath+uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())
        prediction = predict(uploaded_file.name)
        st.success("Dette er et billed af : {}".format(prediction))
    else:
        st.info("Upload et billede")

    
