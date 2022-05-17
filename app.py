import streamlit as st
from predict import show_prediction_page
from statistik import show_statistik_page



page = st.sidebar.selectbox("Vælg en side", ["Forudsigelse", "Statistik"])

if page == "Forudsigelse":
    show_prediction_page()   
else:
    show_statistik_page()
