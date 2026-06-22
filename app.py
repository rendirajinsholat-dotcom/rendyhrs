
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Movie Dashboard", layout="wide")

st.title("🎬 Movie Dashboard")

df = pd.read_csv("movies.csv")

st.sidebar.header("Filter")
genre = st.sidebar.selectbox("Genre", ["Semua"] + sorted(set(",".join(df["Genre"].fillna("")).split(","))))

if genre != "Semua":
    df = df[df["Genre"].str.contains(genre, case=False, na=False)]

st.metric("Jumlah Film", len(df))

col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Film Terpopuler")
    st.dataframe(df.sort_values("Popularity", ascending=False)[["Title","Popularity"]].head(10))

with col2:
    st.subheader("Rating Tertinggi")
    st.dataframe(df.sort_values("Vote_Average", ascending=False)[["Title","Vote_Average"]].head(10))

st.subheader("Data Film")
st.dataframe(df)

st.download_button(
    "Download Data CSV",
    data=df.to_csv(index=False),
    file_name="filtered_movies.csv",
    mime="text/csv"
)
