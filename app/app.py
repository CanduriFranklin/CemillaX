import streamlit as st
import pandas as pd
import joblib

# Cargar el modelo entrenado
model = joblib.load('models/cemillax_uhi_prediction_model.pkl')

# Interfaz de usuario
st.title('Predicción de UHI')

# Entradas del usuario
temp_bronx = st.number_input('Temperatura en el Bronx (°C)')
humidity_bronx = st.number_input('Humedad en el Bronx (%)')
temp_manhattan = st.number_input('Temperatura en Manhattan (°C)')
humidity_manhattan = st.number_input('Humedad en Manhattan (%)')
wind_speed_bronx = st.number_input('Velocidad del viento en el Bronx (m/s)')
wind_speed_manhattan = st.number_input('Velocidad del viento en Manhattan (m/s)')
heat_index_bronx = st.number_input('Índice de calor en el Bronx')
heat_index_manhattan = st.number_input('Índice de calor en Manhattan')
# (Añade más entradas según sea necesario)

# Crear un DataFrame con las entradas
input_data = pd.DataFrame({
    'Air Temp at Surface [degC]_bronx': [temp_bronx],
    'Relative Humidity [percent]_bronx': [humidity_bronx],
    'Air Temp at Surface [degC]_manhattan': [temp_manhattan],
    'Relative Humidity [percent]_manhattan': [humidity_manhattan],
    'Avg Wind Speed [m/s]_bronx': [wind_speed_bronx],
    'Avg Wind Speed [m/s]_manhattan': [wind_speed_manhattan],
    'Heat_Index_bronx': [heat_index_bronx],
    'Heat_Index_manhattan': [heat_index_manhattan],
    # (Añade más columnas según sea necesario)
})

# Hacer la predicción
if st.button('Predecir UHI'):
    prediction = model.predict(input_data)
    st.write(f'Predicción de UHI: {prediction[0]}')