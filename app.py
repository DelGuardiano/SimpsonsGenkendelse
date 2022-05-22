import streamlit as st
from predict import show_prediction_page
from statistik import show_statistik_page
from formerPredictions import show_formerPredictions_page
from login import show_login_page
from dal import *

#currentuser = get_current_user
currentuser = "Bart Simpson"
st.sidebar.write("Du er logget ind som: {}".format(currentuser))
st.sidebar.write("Vælg en side")

page = st.sidebar.selectbox("", ("Login", "Forudsigelse", "Statistik", "Tidligere forudsigelser"))

if page == "Forudsigelse":
    show_prediction_page()
elif page == "Statistik":
    show_statistik_page()
elif page == "Tidligere forudsigelser":
    show_formerPredictions_page()
elif page == "Login":
    show_login_page()

