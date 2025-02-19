import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

data=pd.read_csv("tips.csv")

st.write("Sales Daily Chart")
st.line_chart(data,x="billdate",y="total_bill")

st.divider()

st.scatter_chart(data,x="tip",y="total_bill")

st.divider()

fig, ax= plt.subplots()
ax.hist(data["tip"])
st.pyplot(fig)

st.divider()

a=st.number_input("What is your Salary?")
b=st.number_input("How much is your tax")
if st.button("Calculate"):
    c=a-b
else:
    c=0.00
st.write("My net salary is ", c)


