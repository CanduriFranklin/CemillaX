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
# (Añade más entradas según sea necesario)

# Crear un DataFrame con las entradas
input_data = pd.DataFrame({
    'Air Temp at Surface [degC]_bronx': [temp_bronx],
    'Relative Humidity [percent]_bronx': [humidity_bronx],
    # (Añade más columnas según sea necesario)
})

# Hacer la predicción
if st.button('Predecir UHI'):
    prediction = model.predict(input_data)
    st.write(f'Predicción de UHI: {prediction[0]}')