# OriumSpaceRX: 
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
