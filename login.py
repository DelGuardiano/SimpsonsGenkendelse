import streamlit as st
from dal import *

def show_login_page():     
    st.title("Login")
    st.write("Indtast dit brugernavn og password")
    brugernavn = st.text_input("Brugernavn", value="")
    password = st.text_input("Password" , type="password", value="")
    
    login = st.button("Login")
    opret_ny_bruger = st.button("Opret ny bruger")
        
    find_user = Bruger().find_user(brugernavn, password)

    if find_user == False:
        if login == True:
            st.error ("Brugeren findes ikke")

        elif opret_ny_bruger == True:
            if brugernavn == "" or password == "":                       
                st.error("Indtast et brugernavn og password")           
            else:
                save_new_user(brugernavn, password)
                st.success("Du er nu oprettet en ny bruger")

    elif find_user == True:
        if login == True:
            if brugernavn == "" or password == "":
                st.error("Forkert brugernavn eller password")
            else:          
                st.success("Du er logget ind som: {}".format(brugernavn))    
                
                st.session_state['Brugernavn'] = brugernavn
                st.session_state['load_state'] = login
                
       
        elif opret_ny_bruger == True:
            st.error ("Brugeren findes allerede")

def currentuser():  
    return st.session_state.get('Brugernavn')

def state():
    return st.session_state.get('load_state')
