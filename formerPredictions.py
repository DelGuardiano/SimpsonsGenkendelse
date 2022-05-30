import streamlit as st
import pandas as pd
from dal import *
import matplotlib.pyplot as plt

def load_data():
    df = pd.DataFrame(list(Forudsigelse().get_all()))
    df = df[["Navn", "Billed", "Forfatter", "Oprettelsesdato", "Forudsigelse"]]
    return df

def show_formerPredictions_page():
    df = load_data()
    st.title("Tidligere forudsigelser")
    st.write("Her er de tidligere forudsigelser")   
    st.write(df)

    chart = st.checkbox("Vis diagram")
    if chart:
        df = df.groupby(["Forudsigelse"])["Forudsigelse"].count().sort_values(ascending=False)
        figl, axl = plt.subplots()
        axl.pie(df, labels=df.index, autopct='%1.1f%%')
        axl.axis('equal')
        st.pyplot(figl)




    
    




    

   


        


    

   
    











    

    






     

