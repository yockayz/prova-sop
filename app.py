import streamlit as st
import pandas as pd

df = pd.read_csv("MS_Financial Sample.csv", on_bad_lines='skip')

st.write("Prova SOP - Erick Cardoso Martins")
st.dataframe(df)
