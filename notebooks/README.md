# Exploratory Data Analysis (EDA)

## Overview
This repository contains the code and analysis for the Week 0 Challenge in MoonLight Energy Solutions. This challenge is part of the evaluation for a 12-week training program in Data Engineering (DE), Financial Analytics (FA), and Machine Learning Engineering (MLE). The main components of this repository include:
•	Exploratory Data Analysis (EDA): Analyzing data to uncover trends and patterns.
•	Statistical Analysis: Utilizing statistical techniques to guide data-driven decisions.
•	Streamlit Dashboard: Creating an interactive tool to present key insights.

## Description
The dataset includes the following columns:
- **Timestamp**: Date and time of each observation.
- **GHI**: Global Horizontal Irradiance (W/m²).
- **DNI**: Direct Normal Irradiance (W/m²).
- **DHI**: Diffuse Horizontal Irradiance (W/m²).
- **ModA**: Measurements from a module or sensor (A), similar to irradiance (W/m²).
- **ModB**: Measurements from a module or sensor (B), similar to irradiance (W/m²).
- **Tamb**: Ambient Temperature (°C).
- **RH**: Relative Humidity (%).
- **WS**: Wind Speed (m/s).
- **WSgust**: Wind Gust Speed (m/s).
- **WSstdev**: Wind Speed Standard Deviation (m/s).
- **WD**: Wind Direction (degrees).
- **WDstdev**: Wind Direction Standard Deviation (degrees).
- **BP**: Barometric Pressure (hPa).
- **Cleaning**: Cleaning status of the sensors.
- **Precipitation**: Precipitation (mm).
- **TModA**: Temperature Measurement from Module A (°C).
- **TModB**: Temperature Measurement from Module B (°C).
- **Comments**: Additional comments.

## Steps in the Analysis

1. **Data_Loading_and_Exploration**
   - Libraries: `pandas`.
   - Read the CSV file and display the first few rows.
   - Create an instance of DataProcessor

2. **Summary_Statistics_and_Quality_Check**
   - Create an instance of DataQualityChecker
   - Calculate summary statistics and perform data quality check

3. **Time_Series_Analysis**
   - Create an instance of TimeSeriesAnalyzer

4. **Correlation_and_Wind_Analysis**
   - Create an instance of CorrelationAndWindAnalyzer

5. **Temperature_and_Humidity_Analysis**
   - Analyze the relationship between temperature and relative humidity

6. **Advanced_Analysis_ZScores_and_Bubble_Charts**
   - Create an instance of AdvancedDataAnalyzer
   - Calculate Z-scores and identify outliers
   - Plot bubble charts

7. **Data_Cleaning_and_Preparation**  
   - Create an instance of DataCleaner

  

## Dependencies
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scipy`



