import streamlit as st
from dal import *

def show_login_page():     
    st.title("Login")
    st.write("Indtast dit brugernavn og password")
    brugernavn = st.text_input("Brugernavn")
    password = st.text_input("Password" , type="password")

    login = st.button("Login")
    opret_ny_bruger = st.button("Opret ny bruger")

    
    if login == True:
        if brugernavn == "" or password == "":
            st.error("Forkert brugernavn eller password")
        else:          
            st.success("Du er logget ind som: {}".format(brugernavn))

        return brugernavn

    elif opret_ny_bruger == True:
        if brugernavn == "" or password == "":                       
            st.error("Indtast et brugernavn og password")           
        else:
            save_new_user(brugernavn, password)
            st.success("Du er nu oprettet en ny bruger")