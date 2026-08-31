import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="ChurnLens", layout="wide")

st.title("ChurnLens")
st.write("Explainable Customer Churn Analytics")

df = pd.read_csv("dashboard_data.csv")

col1, col2, col3 = st.columns(3)

col1.metric("Customers", f"{len(df):,}")
col2.metric("Average churn risk", f"{df['PredictedRisk'].mean():.1%}")
col3.metric("High-risk customers", f"{(df['PredictedRisk'] >= 0.65).sum():,}")

st.subheader("Customer risk explorer")

fig = px.scatter(
    df,
    x="MonthlyCharges",
    y="PredictedRisk",
    color="PredictedRisk",
    hover_data=["customerID", "Contract", "tenure"],
    color_continuous_scale="RdYlGn_r"
)

fig.add_hline(y=0.65, line_dash="dash", line_color="red")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Customer data")
st.dataframe(df, use_container_width=True)
