import streamlit as st
from datetime import date

st.title(" Age Calculator")

dob = st.date_input("Enter your Date of Birth:", min_value=date(1900, 1, 1), max_value=date.today())

if dob:
    today = date.today()

    years = today.year - dob.year
    months = today.month - dob.month
    days = today.day - dob.day

    if days < 0:
        months -= 1
        prev_month = today.month - 1 if today.month > 1 else 12
        prev_year = today.year if today.month > 1 else today.year - 1
        days += (date(prev_year, prev_month % 12 + 1, 1) - date(prev_year, prev_month, 1)).days

    if months < 0:
        years -= 1
        months += 12

    st.subheader(" Your Age is:")
    st.write(f"**{years} years, {months} months, {days} days**")
