import unittest
import joblib
from src.train_model import train_model

class TestModel(unittest.TestCase):
    def test_model_training(self):
        # Entrenar el modelo
        train_model('data/processed/NY_Mesonet_Weather_Processed.xlsx', 'models/test_model.pkl')

        # Verificar que el modelo se guardó correctamente
        model = joblib.load('models/test_model.pkl')
        self.assertIsNotNone(model)

if __name__ == "__main__":
    unittest.main()