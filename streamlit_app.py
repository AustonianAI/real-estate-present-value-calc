import streamlit as st
import pandas as pd
import numpy as np

from rentcast import get_property_data, get_rent_data, get_surrounding_properties, get_value_data

import state

st.header('Residential RE Fundamental Value Calculator')

with st.sidebar:
    address_to_analyze = st.text_input(
        'Enter address to analyze', '8109 Castle Peake Trail, Austin, TX 78726')

    if st.button('Analyze', type="primary"):
        st.session_state.prop_data = get_property_data(address_to_analyze)
        st.session_state.rent_data = get_rent_data(st.session_state.prop_data)
        st.session_state.value_data = get_value_data(
            st.session_state.prop_data)
        st.session_state.surrounding_prop_data = get_surrounding_properties(
            st.session_state.prop_data)

    if (st.session_state.prop_data is not None):
        st.subheader('Property Info')
        st.markdown(
            f'**Address:** {st.session_state.prop_data.get("formattedAddress")}')
        st.markdown(
            f'**Square Footage:** {st.session_state.prop_data.get("squareFootage")}')
        st.markdown(
            f'**Bathrooms:** {st.session_state.prop_data.get("bathrooms")}')
        st.markdown(
            f'**Bedrooms:** {st.session_state.prop_data.get("bedrooms")}')
        st.markdown(
            f'**Property Type:** {st.session_state.prop_data.get("propertyType")}')
        st.markdown(
            f'**Rent Estimate:** {st.session_state.rent_data.get("rent")}')
        st.markdown(
            f'**Price Estimate:** {st.session_state.value_data.get("price")}')


with st.form(key="inputs"):
    price, tax, finance, costs, market, analyze = st.tabs(
        ["Rent/Sale Pricing", "Taxes", "Financing", "Operating Costs", "Market Assumptions", "Analyze"])

    with price:
        st.subheader('Rent and Sale Pricing')
        col1, col2 = st.columns(2)
        with col1:
            rent = st.slider('Rent Price (monthly)', min_value=int(st.session_state.rent_data.get('rentRangeLow', 0)), max_value=int(
                st.session_state.rent_data.get('rentRangeHigh', 100000)), value=int(st.session_state.rent_data.get('rent', 0)), step=10, format="$%d")
        with col2:
            price = st.slider('Sale Price', min_value=int(st.session_state.value_data.get('priceRangeLow', 0) * .75), max_value=int(st.session_state.value_data.get('priceRangeHigh', 999999999) * 1.25), value=st.session_state.get(
                "value_data")['price'], step=1000, format="$%d")

    with tax:
        st.subheader('Taxes')
        tax_rate = st.number_input('Tax Rate (%)', value=1.5)
        tax_rate /= 100

    with analyze:
        st.form_submit_button(label="Submit")
