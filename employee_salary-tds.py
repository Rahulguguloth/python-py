import streamlit as st

st.title("Income Tax Calculator ")

# Input salary from user
salary = st.number_input("Enter your salary:")

total = 0
remaining = salary

if remaining >= 500000:
    remaining -= 300000

    # 5% on next 300,000
    if remaining >= 300000:
        total += 300000 * 0.05
        remaining -= 300000
    else:
        total += remaining * 0.05
        remaining = 0

    # 10% on next 300,000
    if remaining >= 300000:
        total += 300000 * 0.1
        remaining -= 300000
    else:
        total += remaining * 0.1
        remaining = 0

    # 15% on next 600,000
    if remaining >= 600000:
        total += 600000 * 0.15
        remaining -= 600000
    else:
        total += remaining * 0.15
        remaining = 0

    # 30% on anything above
    if remaining > 0:
        total += remaining * 0.3

# Show result
st.subheader("Total Tax (TDS):")
st.write(f"₹ {total:,.2f}")
