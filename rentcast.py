import streamlit as st

import requests
from dotenv import load_dotenv
import os

load_dotenv()


RC_HEADERS = {
    "Accept": "application/json",
    "X-Api-Key": os.getenv("RC_API_KEY"),
}


@st.cache_data
def get_property_data(address):
    url = "https://api.rentcast.io/v1/properties"
    params = {
        "address": address,
    }

    response = requests.get(url, headers=RC_HEADERS, params=params)

    if response.status_code != 200:
        raise Exception("Property Data API call failed")

    return response.json()[0]


@st.cache_data
def get_rent_data(prop_data):
    url = "https://api.rentcast.io/v1/avm/rent/long-term"
    params = {
        'address': prop_data.get('formattedAddress'),
        'propertyType': prop_data.get('propertyType'),
        'bedrooms': prop_data.get('bedrooms'),
        "bathrooms":  prop_data.get('bathrooms'),
        "squareFootage":  prop_data.get('squareFootage'),
        "maxRadius": 10,
        "daysOld": 250,
        "compCount": 25
    }

    response = requests.get(url, headers=RC_HEADERS, params=params)

    if response.status_code != 200:
        raise Exception("Rent Data API call failed")

    return response.json()


@st.cache_data
def get_value_data(prop_data):
    url = "https://api.rentcast.io/v1/avm/value"
    params = {
        'address': prop_data.get('formattedAddress'),
        'propertyType': prop_data.get('propertyType'),
        'bedrooms': prop_data.get('bedrooms'),
        "bathrooms":  prop_data.get('bathrooms'),
        "squareFootage":  prop_data.get('squareFootage'),
        "maxRadius": 10,
        "daysOld": 250,
        "compCount": 10
    }

    response = requests.get(url, headers=RC_HEADERS, params=params)

    if response.status_code != 200:
        raise Exception("Rent Data API call failed")

    return response.json()


@st.cache_data
def get_surrounding_properties(prop_data):
    url = "https://api.rentcast.io/v1/properties"
    params = {
        'address': prop_data.get('formattedAddress'),
        'propertyType': prop_data.get('propertyType'),
        'radius': 2,
        'limit': 500
    }

    response = requests.get(url, headers=RC_HEADERS, params=params)

    if response.status_code != 200:
        raise Exception("Rent Data API call failed")

    return response.json()
