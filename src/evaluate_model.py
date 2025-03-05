import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
import joblib

def evaluate_model(model_file, data_file):
    # Cargar el modelo entrenado
    model = joblib.load(model_file)

    # Cargar los datos de prueba
    df = pd.read_excel(data_file)
    X_test = df.drop('UHI', axis=1)
    y_test = df['UHI']

    # Hacer predicciones
    y_pred = model.predict(X_test)

    # Evaluar el modelo
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    return mse, r2

if __name__ == "__main__":
    mse, r2 = evaluate_model('models/uhi_prediction_model.pkl', 'data/processed/NY_Mesonet_Weather_Processed.xlsx')
    print(f'MSE: {mse}')
    print(f'R²: {r2}')