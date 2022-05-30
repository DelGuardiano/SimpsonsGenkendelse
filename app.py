import webbrowser
import streamlit as st
from predict import show_prediction_page
from statistik import show_statistik_page
from formerPredictions import show_formerPredictions_page
from login import show_login_page, currentuser

st.session_state.currentuser = currentuser()

if st.session_state.currentuser == None:
    show_login_page()   

if st.session_state.currentuser != None: 
    st.sidebar.write("Du er logget ind som: {}".format(st.session_state.currentuser))
    st.sidebar.write("Vælg en side")

    page = st.sidebar.selectbox("", ("Forudsigelse", "Statistik", "Tidligere forudsigelser"))

    if page == "Forudsigelse":
        show_prediction_page()
    elif page == "Statistik":
        show_statistik_page()
    elif page == "Tidligere forudsigelser":
        show_formerPredictions_page()

    logud = st.sidebar.button("Log ud")
    if logud:
        st.session_state.currentuser = None
        page = None
        st.sidebar.success("Du er nu logget ud")
        
        
        
        


        
             
        
     

     
        
   
        
        




