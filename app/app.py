import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('models/cemillax_uhi_prediction_model.pkl')

# User interface
st.title('UHI Prediction')

# User inputs
temp_bronx = st.number_input('Temperature in the Bronx (°C)')
humidity_bronx = st.number_input('Humidity in the Bronx (%)')
wind_speed_bronx = st.number_input('Wind speed in the Bronx (m/s)')
wind_direction_bronx = st.number_input('Wind direction in the Bronx (degrees)')
solar_flux_bronx = st.number_input('Solar flux in the Bronx (W/m^2)')
temp_manhattan = st.number_input('Temperature in Manhattan (°C)')
humidity_manhattan = st.number_input('Humidity in Manhattan (%)')
wind_speed_manhattan = st.number_input('Wind speed in Manhattan (m/s)')
wind_direction_manhattan = st.number_input('Wind direction in Manhattan (degrees)')
solar_flux_manhattan = st.number_input('Solar flux in Manhattan (W/m^2)')
heat_index_bronx = st.number_input('Heat index in the Bronx')
heat_index_manhattan = st.number_input('Heat index in Manhattan')
# (Add more inputs as needed)

# Create a DataFrame with the inputs
input_data = pd.DataFrame({
    'Air Temp at Surface [degC]_bronx': [temp_bronx],
    'Relative Humidity [percent]_bronx': [humidity_bronx],
    'Avg Wind Speed [m/s]_bronx': [wind_speed_bronx],
    'Wind Direction [degrees]_bronx': [wind_direction_bronx],
    'Solar Flux [W/m^2]_bronx': [solar_flux_bronx],
    'Air Temp at Surface [degC]_manhattan': [temp_manhattan],
    'Relative Humidity [percent]_manhattan': [humidity_manhattan],
    'Avg Wind Speed [m/s]_manhattan': [wind_speed_manhattan],
    'Wind Direction [degrees]_manhattan': [wind_direction_manhattan],
    'Solar Flux [W/m^2]_manhattan': [solar_flux_manhattan],
    'Heat_Index_bronx': [heat_index_bronx],
    'Heat_Index_manhattan': [heat_index_manhattan],
    # (Add more columns as needed)
})

# Make the prediction
if st.button('Predict UHI'):
    prediction = model.predict(input_data)
    st.write(f'UHI Prediction: {prediction[0]}')