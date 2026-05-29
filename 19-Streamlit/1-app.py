import streamlit as st
import pandas as pd
import numpy as np


## Title of the Application
st.title("My First Streamlit App")

## Display a simple text
st.write("This is a simple text displayed using Streamlit.")


## Create a Dataframe

df=pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})


## Display the Dataframe
st.write("Here is a simple DataFrame:")
st.write(df)


## Create a line chart
st.write("Here is a simple Line Chart:")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)