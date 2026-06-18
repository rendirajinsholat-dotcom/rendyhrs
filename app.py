5
6
5
6
5
6
5
6
5
6
5
6
5
6
5
6
5
6
5
6
5
6
5
6import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="EV Adoption Dashboard",
    layout="wide"
)

st.title("🚗 Dashboard Analisis Adopsi Kendaraan Listrik")

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("global_ev_adoption_behavior_2026.csv")

df = load_data()

# Sidebar
st.sidebar.header("Filter Data")

city = st.sidebar.multiselect(
    "Pilih Tipe Kota",
    options=df["city_type"].unique(),
    default=df["city_type"].unique()
)

education = st.sidebar.multiselect(
    "Pilih Pendidikan",
    options=df["education_level"].unique(),
    default=df["education_level"].unique()
)

filtered_df = df[
    (df["city_type"].isin(city)) &
    (df["education_level"].isin(education))
]

# KPI
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Jumlah Data", len(filtered_df))

with col2:
    st.metric(
        "Rata-rata Income",
        f"${filtered_df['annual_income'].mean():,.0f}"
    )

with col3:
    st.metric(
        "Rata-rata EV Adoption",
        f"{filtered_df['ev_adoption_likelihood'].mean():.2f}"
    )

st.divider()

# Histogram
fig1 = px.histogram(
    filtered_df,
    x="ev_adoption_likelihood",
    nbins=30,
    title="Distribusi EV Adoption Likelihood"
)

st.plotly_chart(fig1, use_container_width=True)

# Scatter Plot
fig2 = px.scatter(
    filtered_df.sample(3000),
    x="annual_income",
    y="ev_adoption_likelihood",
    color="city_type",
    title="Income vs EV Adoption"
)

st.plotly_chart(fig2, use_container_width=True)

# Correlation
numeric_df = filtered_df.select_dtypes(include="number")

corr = numeric_df.corr()

fig3 = px.imshow(
    corr,
    text_auto=True,
    aspect="auto",
    title="Correlation Heatmap"
)

st.plotly_chart(fig3, use_container_width=True)

# Data Table
st.subheader("Dataset")
st.dataframe(filtered_df)
5
6
5
6
5
6
