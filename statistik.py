import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from dal import Karakterer
from tensorflow import keras
from localPath import *
from PIL import Image

@st.cache
def load_data():
    df = pd.DataFrame(list(Karakterer().get_all()))
    df = df[["name", "total", "train", "test"]]
    return df

df = load_data()


def show_statistik_page():
    st.title("Statistik")
    st.subheader("Statistik over billeder af Simpsons karakterer")
    st.write(df)

    st.write("""#### Antal billeder af Simpsons karakterer i alt ####""")

    data = df.groupby(["name"])["total"].mean().sort_values(ascending=False)
    st.bar_chart(data)

    st.write("""####  Antal billeder af Simpsons karakterer brugt til træningen af modellen ####""")
    data = df.groupby(["name"])["train"].mean().sort_values(ascending=False)
    figl, axl = plt.subplots()
    axl.pie(data, labels=data.index, autopct='%1.1f%%')
    axl.axis('equal')
    st.pyplot(figl)

    st.write("""####  Antal billeder brugt i test af modellen ####""")
    data = df.groupby(["name"])["test"].mean().sort_values(ascending=False)
    st.line_chart(data)

    st.write("""#### Diagram over accuracy for modellen ####""")
    data = Image.open(legendplot)
    st.image(data, width=500)

    st.write("""#### Diagram over accuracy for modellen ####""")
    data = Image.open(boxplot)
    st.image(data, width=500)

    
    
    

    
