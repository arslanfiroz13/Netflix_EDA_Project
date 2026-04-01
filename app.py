import streamlit as st
import pandas as pd

st.title("Netflix Data Analysis Dashboard")

df = pd.read_csv(r"C:\Users\Arslan firoz\OneDrive\Desktop\Netflix_EDA_Project\notebook\clean_netflix_data.csv")

st.write("Full Dataset")
st.dataframe(df)