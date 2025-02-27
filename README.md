# OriumX:
Urban Heat Island Index (UHI) prediction

# Project Description:
The objective of this project is to develop a predictive model to estimate the Urban Heat
Island Index (UHI) in urban areas, using meteorological and environmental data.
Furthermore, the model is designed to identify and highlight key factors that significantly contribute to the development of UHI hotspots.

# Data Used / Data Source:
## Meteorological Data: 
Provided by the New York State Mesonet.

Includes measurements of temperature, relative humidity, wind speed, wind direction, and solar flux.

Two locations: Bronx and Manhattan.

Ground Track Data: Temperature measurements taken at different points in the city.

# Data structure
## Bronx and Manhattan:

# Date/Time:
Date and time of measurement.

Surface air temperature [degrees C]: Air temperature near the surface.

Relative humidity [percent]: Relative humidity.

Average wind speed [m/s]: Average wind speed.

Wind direction [degrees]: Wind direction.

Solar flux [W/m^2]: Solar flux at the surface.

# Data Processing
# Steps Performed
# Data Loading:

## Data was loaded from an Excel file containing two sheets: 
Bronx and Manhattan.

## Cleaning and Preprocessing:

Converting the Date/Time column to datetime type.

Combining the data from both locations.

Calculating the UHI as the temperature difference between the Bronx and Manhattan.

Calculating the Heat Index for both locations.

Feature Selection:

Relevant features for the model were selected, such as temperature, humidity, wind speed, solar flux, etc.

# Modeling
# Algorithm Used
## Random Forest Regressor: 
A decision tree-based machine learning model, suitable for regression problems.

## Model Training
The data was split into training (80%) and test (20%) sets.

The model was trained using the training set.

The performance of the model was evaluated using metrics such as MSE (Mean Square Error) and R² (Coefficient of Determination).

Model Results
MSE: 0.0528

R²: 0.9675

These results indicate that the model is highly predictive and explains approximately 96.75% of the variability in the data.

# User Interface with Streamlit
A simple interface was developed for users to enter data and obtain UHI predictions.

## Features
Input fields for meteorological characteristics.

Button to make the prediction.

Display of the prediction and the entered data.

# Repository Structure: OriumX
orium-x/
│
├── data/                       # Folder to store data
│ ├── raw/                      # Raw (unprocessed) data
│ ├── processed/                # Processed data
│ └── external/                 # External data (if any)
│
├── models/                     # Trained models
│ └── uhi_prediction_model.pkl  # Saved model
│
├── notebooks/                  # Jupyter/Colab notebooks
│ ├── 01_data_exploration.ipynb
│ ├── 02_model_training.ipynb
│ └── 03_model_evaluation.ipynb
│
├── src/ # Source code (scripts)
│ ├── data_processing.py         # Script to process data
│ ├── train_model.py             # Script to train the model
│ ├── evaluate_model.py          # Script to evaluate the model
│ └── predict.py                 # Script to make predictions
│
├── tests/                       # Unit tests
│ ├── test_data_processing.py
│ ├── test_model.py
│ └── __init__.py
│
├── app/                          # Application (Streamlit, Flask, etc.)
│ ├── app.py                      # Main application script
│ ├── templates/                  # HTML templates (if it's a web API)
│ └── static/                     # Static files (CSS, JS, images)
│
├── docs/                         # Project documentation
│ ├── README.md                   # Project overview
│ ├── requirements.txt            # Project dependencies
│ └── images/                     # Images for documentation
│
├── .gitignore                    # Files and folders ignored by Git
├── LICENSE                       # Project license
└── README.md                     # Main README file

# Explanation of the Structure:

## 1. data/
# raw/: 
Stores the raw data (e.g. the original Excel file NY_Mesonet_Weather_New_Data.xlsx).

# processed/: 
Stores the processed data (e.g. the NY_Mesonet_Weather_Processed.xlsx file).

# external/: 
External data that is not part of the main dataset (optional).

## 2. models/
Stores the trained models (e.g. Oriumx_uhi_prediction_model.pkl).

## 3. notebooks/
Contains the Jupyter or Google Colab notebooks used to explore data, train models, and evaluate results.

### 01_data_exploration.ipynb: 
Exploratory data analysis (EDA).

### 02_model_training.ipynb: 
Model training.

### 03_model_evaluation.ipynb: 
Model evaluation and results visualization.

## 4. src/
Contains Python scripts to automate tasks:

### Data_processing.py: 
Processes raw data and prepares it for the model.

### Train_model.py: 
Trains the model and saves it to the models/ folder.

### Evaluate_model.py: 
Evaluates the model and generates metrics.

### Predict.py: 
Makes predictions using the trained model.

## 5. tests/
Contains unit tests to validate the code:

### test_data_processing.py: 
Tests for the data processing script.

### test_model.py: 
Tests for the trained model.

## 6. app/
Contains the application to interact with the model:

### app.py: 
Main script of the application (for example, an API with Flask or an interface with Streamlit).

### templates/: 
HTML templates if the application is a web API.

### static/: 
Static files (CSS, JS, images) if the application is a web API.

## 7. docs/
Contains the project documentation:

### README.md: 
Project overview.

### requirements.txt: 
List of project dependencies.

### images/: 
Images used in the documentation.

## 8. Files in the Root
### .gitignore: 
Specifies files and folders that Git should ignore (for example, virtual environment files or sensitive data).

### LICENSE: 
Project license (for example, MIT, Apache, etc.).

## README.md: 
Main README file describing the project.
