import streamlit as st
import pandas as pd

df = pd.read_csv("MS_Financial Sample.csv", sep=";", on_bad_lines="skip")

# Limpeza de nomes de colunas para remover espaços extras
df.columns = df.columns.str.strip()

segment_counts = df["Segment"].value_counts().reset_index()
segment_counts.columns = ["Segment", "Count"]

top_5_segments = segment_counts.head(5)

st.title("Os 5 Segmentos Mais Frequentes no Dataset")

st.write("### Tabela dos 5 Segmentos Mais Frequentes")
st.dataframe(top_5_segments)

st.write("### Gráfico dos 5 Segmentos Mais Frequentes")
st.bar_chart(top_5_segments.set_index("Segment"))