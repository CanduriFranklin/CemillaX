import unittest
import joblib
import pandas as pd
from src.train_model import train_model

class TestModel(unittest.TestCase):
    def test_model_training(self):
        # Entrenar el modelo
        train_model('data/processed/NY_Mesonet_Weather_Processed.xlsx', 'models/test_model.pkl')

        # Verificar que el modelo se guardó correctamente
        model = joblib.load('models/test_model.pkl')
        self.assertIsNotNone(model)

    def test_model_predictions(self):
        # Cargar el modelo
        model = joblib.load('models/test_model.pkl')
        
        # Cargar los datos de prueba
        df = pd.read_excel('data/processed/NY_Mesonet_Weather_Processed.xlsx')
        X_test = df.drop('UHI', axis=1)
        
        # Hacer predicciones
        predictions = model.predict(X_test)
        
        # Verificar que se hicieron predicciones
        self.assertEqual(len(predictions), len(X_test))

if __name__ == "__main__":
    unittest.main()