import streamlit as st

from currency import currency_converter
from unit import (
    length_converter,
    weight_converter,
    temperature_converter
)

st.set_page_config(
    page_title="Currency & Unit Converter",
    page_icon="🔄",
    layout="centered"
)

st.title("🔄 Currency & Unit Converter")
st.write("Convert currencies and different units easily.")
converter_type = st.selectbox(
    "Choose Converter",
    [
        "Currency",
        "Length",
        "Weight",
        "Temperature"
    ]
)

if converter_type == "Currency":

    st.subheader("💱 Currency Converter")

    amount = st.number_input(
        "Enter Amount",
        min_value=0.0,
        value=100.0
    )

    from_currency = st.selectbox(
        "From Currency",
        ["INR", "USD", "EUR", "GBP", "JPY", "AUD", "CAD"]
    )

    to_currency = st.selectbox(
        "To Currency",
        ["INR", "USD", "EUR", "GBP", "JPY", "AUD", "CAD"]
    )

    if st.button("Convert"):

        result = currency_converter(
            amount,
            from_currency,
            to_currency
        )

        if isinstance(result, str):
            st.error(result)
        else:
            st.success(
                f"{amount:g} {from_currency} = "
                f"{result:.2f} {to_currency}"
            )

elif converter_type == "Length":

    st.subheader("📏 Length Converter")

    value = st.number_input(
        "Enter Value",
        min_value=0.0,
        value=1.0
    )

    units = [
        "meter",
        "kilometer",
        "centimeter",
        "mile",
        "foot"
    ]

    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)

    if st.button("Convert"):

        result = length_converter(
            value,
            from_unit,
            to_unit
        )

        if isinstance(result, str):
            st.error(result)
        else:
            st.success(
                f"{value:g} {from_unit} = "
                f"{result:.2f} {to_unit}"
            )

elif converter_type == "Weight":

    st.subheader("⚖️ Weight Converter")

    value = st.number_input(
        "Enter Value",
        min_value=0.0,
        value=1.0
    )

    units = [
        "kilogram",
        "gram",
        "pound",
        "ounce"
    ]

    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)

    if st.button("Convert"):

        result = weight_converter(
            value,
            from_unit,
            to_unit
        )

        if isinstance(result, str):
            st.error(result)
        else:
            st.success(
                f"{value:g} {from_unit} = "
                f"{result:.2f} {to_unit}"
            )

elif converter_type == "Temperature":

    st.subheader("🌡️ Temperature Converter")

    value = st.number_input(
        "Enter Temperature",
        value=0.0
    )

    units = [
        "celsius",
        "fahrenheit",
        "kelvin"
    ]

    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)

    if st.button("Convert"):

        result = temperature_converter(
            value,
            from_unit,
            to_unit
        )

        if isinstance(result, str):
            st.error(result)
        else:
            st.success(
                f"{value:g} {from_unit} = "
                f"{result:.2f} {to_unit}"
            )
st.divider()
st.caption("Built with Python 🐍 and Streamlit 🚀")
