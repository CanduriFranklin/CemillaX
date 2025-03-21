import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

def train_model(input_file, output_file):
    # Cargar los datos procesados
    df = pd.read_excel(input_file)

    # Separar características (X) y variable objetivo (y)
    X = df.drop('UHI', axis=1)
    y = df['UHI']

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entrenar el modelo
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Guardar el modelo
    joblib.dump(model, output_file)

if __name__ == "__main__":
    train_model('../data/processed/NY_Mesonet_Weather_Processed.xlsx', '../models/uhi_prediction_model.pkl')