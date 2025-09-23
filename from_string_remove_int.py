import streamlit as st

st.title("remove the integers from string")

s = st.text_input("Enter some text:")

r = ""
for ch in s:
    if not (ord(ch) >= 48 and ord(ch) <= 57):  
        r += ch

st.write("Output without numbers:", r)
