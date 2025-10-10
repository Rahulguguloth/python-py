import streamlit as st

# Fuel data
fuels = {"1": ("Petrol", 110), "2": ("Diesel", 95)}

# Function to calculate bill
def calc_bill(ft, ltr):
    price = fuels[ft][1]
    sub = ltr * price
    disc = 200 if ltr > 50 else 0
    tot = sub - disc
    return sub, disc, tot

# Streamlit UI
st.set_page_config(page_title="Petrol Pump Billing System", page_icon="", layout="centered")

st.title(" Petrol Pump Billing System")

# Fuel selection
fuel_type = st.selectbox("Select Fuel Type", options=["Petrol", "Diesel"])
ft = "1" if fuel_type == "Petrol" else "2"

# Price info
st.info(f" Price per Litre: ₹{fuels[ft][1]}")

# Litres input
litres = st.number_input("Enter litres to fill:", min_value=0.0, max_value=100.0, step=0.5)

# Calculate button
if st.button("Generate Bill"):
    if litres == 0:
        st.warning("Please enter litres greater than 0.")
    else:
        sub, disc, tot = calc_bill(ft, litres)

        # Display Receipt
        st.subheader(" Fuel Receipt")
        st.write("---")
        st.write(f"*Fuel Type:* {fuel_type}")
        st.write(f"*Litres Filled:* {litres:.2f} L")
        st.write(f"*Price per Litre:* ₹{fuels[ft][1]}")
        st.write(f"*Subtotal:* ₹{sub:.2f}")
        st.write(f"*Discount Applied:* ₹{disc}")
        st.write(f"*Total Payable:* ₹{tot:.2f}")
        st.success(" Transaction Completed Successfully!")

st.write("---")
st.caption("Thank you for visiting ")
