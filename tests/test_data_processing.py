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

    def test_processed_data_content(self):
        # Cargar los datos procesados
        df = pd.read_excel('data/processed/test_processed.xlsx')
        
        # Verificar que las columnas esperadas existen
        expected_columns = [
            'Date / Time', 'Air Temp at Surface [degC]_bronx', 'Air Temp at Surface [degC]_manhattan', 'UHI'
        ]
        for column in expected_columns:
            self.assertIn(column, df.columns)

if __name__ == "__main__":
    unittest.main()