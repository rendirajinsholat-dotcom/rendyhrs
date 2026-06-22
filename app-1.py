import streamlit as st
import pandas as pd

st.set_page_config(page_title="Movie Dashboard", layout="wide")

st.title("🎬 Movie Dashboard")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("mymoviedb.csv")

st.write("Jumlah data:", len(df))

st.subheader("Preview Data")
st.dataframe(df.head())

st.subheader("Filter Film")
if "Title" in df.columns:
    keyword = st.text_input("Cari judul film")
    if keyword:
        df = df[df["Title"].str.contains(keyword, case=False, na=False)]

st.dataframe(df)

st.subheader("Statistik")
num_cols = df.select_dtypes(include="number").columns
if len(num_cols) > 0:
    col = st.selectbox("Pilih kolom numerik", num_cols)
    st.bar_chart(df[col].head(20))
