import unittest
import pandas as pd
from src.data_processing import process_data

class TestDataProcessing(unittest.TestCase):
    def test_process_data(self):
        # Procesar los datos
        process_data('data/raw/NY_Mesonet_Weather_New_Data.xlsx', 'data/processed/test_processed.xlsx')

        # Verificar que el archivo procesado existe
        df = pd.read_excel('data/processed/test_processed.xlsx')
        self.assertFalse(df.empty)

if __name__ == "__main__":
    unittest.main()