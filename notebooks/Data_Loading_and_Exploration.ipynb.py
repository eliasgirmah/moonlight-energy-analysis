#!/usr/bin/env python
# coding: utf-8

# In[6]:


# 1_Data_Loading_and_Exploration.ipynb

import pandas as pd

class DataProcessor:
    def __init__(self, file_paths):
        self.data = {country: pd.read_csv(path) for country, path in file_paths.items()}
    
    def initial_exploration(self):
        for country, df in self.data.items():
            print(f"Initial exploration for {country}:")
            print(df.head())
            print(df.info())
            print(df.describe())
            print("\n")

# Define file paths for the datasets
file_paths = {
    'benin-malanville': 'C:/Users/user/Documents/10acadamy/data/benin-malanville.csv',
    'sierraleone-bumbuna': 'C:/Users/user/Documents/10acadamy/data/sierraleone-bumbuna.csv',
    'togo-dapaong_qc': 'C:/Users/user/Documents/10acadamy/data/togo-dapaong_qc.csv'
}

# Create an instance of DataProcessor
processor = DataProcessor(file_paths)

# Perform initial exploration
processor.initial_exploration()


# In[ ]:




