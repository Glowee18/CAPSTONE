import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()


data=pd.read_csv("CAPSTONEDATA.csv")
st.title("Capstone Data")

st.write("Other Income by Country")
st.line_chart(data,x="COUNTRY",y="OTHERINCOME")
st.divider()

st.write("Profit After Tax:")
st.bar_chart(data,x="COUNTRY",y="PROFITAFTERTAX", color="#66FFFF")
st.divider()

st.write("Tax Due:")
fig, ax= plt.subplots()
ax.hist(data["TAXDUE"], color ="#FFCC99")
st.pyplot(fig)
st.divider()

st.write("Earning After Tax")
st.scatter_chart(data,x="PROFITAFTERTAX",y="RETAINEDEARNINGS", color="#FFFF00")

