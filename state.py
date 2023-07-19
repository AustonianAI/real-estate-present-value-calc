import streamlit as st

# List of variable names
variable_names = ['prop_data', 'rent_data', 'value_data',
                  'surrounding_prop_data', 'price', 'rent']

# Initialize the variables in the session state
for var in variable_names:
    if var not in st.session_state:
        st.session_state[var] = None
