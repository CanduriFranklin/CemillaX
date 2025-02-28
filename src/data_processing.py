import pandas as pd

def process_data(input_file, output_file):
    # Cargar los datos crudos
    df_bronx = pd.read_excel(input_file, sheet_name='Bronx')
    df_manhattan = pd.read_excel(input_file, sheet_name='Manhattan')

    # Procesar los datos (ejemplo: calcular UHI)
    df_combined = pd.merge(df_bronx, df_manhattan, on='Date / Time', suffixes=('_bronx', '_manhattan'))
    df_combined['UHI'] = df_combined['Air Temp at Surface [degC]_bronx'] - df_combined['Air Temp at Surface [degC]_manhattan']

    # Guardar los datos procesados
    df_combined.to_excel(output_file, index=False)

if __name__ == "__main__":
    process_data('data/raw/NY_Mesonet_Weather_New_Data.xlsx', 'data/processed/NY_Mesonet_Weather_Processed.xlsx')