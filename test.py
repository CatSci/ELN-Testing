import streamlit as st
import pandas as pd

st.header('Testing')

# Cache the dataframe so it's only loaded once

def load_data():
    return pd.DataFrame(
        {
            "Name": 'abc',
            "Molecular Formula": "H20",
            "Molecular Weight": [20],
            "Smile" :"HHO",
            "Density": [10],
            "Hazard": "xyz",
            "Category": "Red"
        }
    )

df = load_data()

st.write('Dataframe')
st.dataframe(df)


st.write('JSON format')

st.json({
    "Name": 'abc',
    "Molecular Formula": "H20",
    "Molecular Weight": 20,
    "Smile" :"HHO",
    "Density": 10,
    "Hazard": "xyz",
    "Category": "Red"
})