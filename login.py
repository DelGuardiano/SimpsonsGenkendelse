import streamlit as st
from dal import *


def show_login_page():     
    st.title("Login")
    st.write("Indtast dit brugernavn og password")
    brugernavn = st.text_input("Brugernavn", value="")
    password = st.text_input("Password" , type="password", value="")
    
    find_user = Bruger().find_user(brugernavn, password)
    login = st.button("Login")
    opret_ny_bruger = st.button("Opret ny bruger")
        
    if find_user == False:
        if login:
            st.error ("Brugeren findes ikke/password er forkert")

        elif opret_ny_bruger:
            if brugernavn == "" or password == "":                       
                st.error("Indtast et brugernavn og password")           
            else:
                save_new_user(brugernavn, password)
                st.success("Du er nu oprettet en ny bruger")

    else:
        if login:                    
                st.success("Du er logget ind som: {}".format(brugernavn))                   
                st.session_state['Brugernavn'] = brugernavn
                st.experimental_rerun()

        elif opret_ny_bruger:
            st.error ("Brugeren findes allerede")

def currentuser():  
    return st.session_state.get('Brugernavn')



