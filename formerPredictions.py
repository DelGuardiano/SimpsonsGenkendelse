from matplotlib import image
import streamlit as st
import pandas as pd
from dal import *

@st.cache
def load_data():
    df = pd.DataFrame(list(Forudsigelse().get_all()))
    df = df[["Navn", "Billed", "Forfatter", "Oprettelsesdato"]]
    return df

df = load_data() 

def show_formerPredictions_page():
    st.title("Tidligere forudsigelser")
    st.write("Her er de tidligere forudsigelser")   
    st.write(df)

     

