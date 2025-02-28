import pandas as pd
import joblib

def predict(model_file, input_data):
    # Cargar el modelo entrenado
    model = joblib.load(model_file)

    # Hacer la predicción
    prediction = model.predict(input_data)
    return prediction

if __name__ == "__main__":
    # Ejemplo de datos de entrada
    input_data = pd.DataFrame({
        'Air Temp at Surface [degC]_bronx': [20.5],
        'Relative Humidity [percent]_bronx': [70.0],
        # (Añade más columnas según sea necesario)
    })

    # Hacer la predicción
    prediction = predict('models/uhi_prediction_model.pkl', input_data)
    print(f'Predicción de UHI: {prediction[0]}')