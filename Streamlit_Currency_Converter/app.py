import streamlit as st
import requests
from frankfurter import get_currencies_list, get_latest_rates, get_historical_rate
from currency import format_output, hist_format_output

url = 'https://www.frankfurter.app/'

# Display Streamlit App Title
st.title("FX Converter")

# Add sidebar
with st.sidebar:
    st.subheader("About This Project")
    st.text("This currency converter uses" + "\n" + "Frankfurter; an open-source API" + "\n" + 
            "for current and historical" + "\n" + "foreign exchange rates.")
    st.text("It allows the user to choose" + "\n" + "the amount to be converted, as" + "\n" + 
            "well as the from and to currencies." + "\n" + "\n" + "There is also an option to select" + 
            "\n" + "a date from the past and retrieve" + "\n" + "the conversion rate from that day.")
    st.subheader("Created By")
    st.text("Denneya Muscat" + "\n" + "24418042")

# Get the list of available currencies from Frankfurter
st.header("List of Available Currencies")
st.json(get_currencies_list())

# If the list of available currencies is None, display an error message in Streamlit App
if get_currencies_list() is None:
    st.error("There are no available currencies")

# Add input fields for capturing amount, from and to currencies
st.header("Conversion Calculator")
from_amount = st.number_input("Amount to Convert")
from_currency = st.selectbox("From Currency", get_currencies_list())
to_currency = st.selectbox("To Currency", get_currencies_list())

# Add a button to get and display the latest rate for selected currencies and amount
if st.button("Get Latest Rate"):
    conversion_rate, date = get_latest_rates(from_currency, to_currency)
    if from_amount == 0:
        st.error("Please enter in the amount you wish to convert")
    else:
        st.subheader("Latest Conversion Rate")
        st.text(format_output(from_amount, from_currency, to_currency, conversion_rate, date))

# Add a date selector (calendar)
from_date = st.date_input("Select Date")

# Add a button to get and display the historical rate for selected date, currencies and amount
if st.button("Get Historical Rate"):
    hist_conversion_rate, from_date = get_historical_rate(from_currency, to_currency, from_date)
    if from_amount == 0:
        st.error("Please enter in the amount you wish to convert")
    else:
        st.subheader("Historical Conversion Rate")
        st.text(hist_format_output(from_amount, from_currency, to_currency, hist_conversion_rate, from_date))



