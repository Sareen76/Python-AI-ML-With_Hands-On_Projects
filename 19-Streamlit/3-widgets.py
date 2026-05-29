import streamlit as st

st.title("Streamlit Widgets")


name = st.text_input("Enter your name")
age = st.slider("Select your age", 0, 100, 25) 

options = ["Js", "CSS", "HTML", "Python"]
choice = st.selectbox("Select your favorite programming language", options)

uploaded_file = st.file_uploader("Upload a file", type=["txt", "csv", "xlsx"])


## if name is not empty then only it will print the message
if name:
    st.write(f"Hello, {name}!")

if age:
    st.write(f"Your age is {age}")

if choice:
    st.write(f"Your favorite programming language is {choice}")

if uploaded_file is not None:
    st.write(f"File {uploaded_file.name} uploaded successfully!")






# ***********GO To streamlit.io and checkout all the UI *****************