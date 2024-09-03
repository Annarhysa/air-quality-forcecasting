import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import streamlit as st

# Load the data
url = 'path_to_your_downloaded_data/aqi-data.csv'
data = pd.read_csv(url)

# Preprocessing
data['date'] = pd.to_datetime(data['date'])
data['year'] = data['date'].dt.year
data['month'] = data['date'].dt.month

# Handling missing values
data.fillna(method='ffill', inplace=True)

# Aggregate data by month and year
monthly_data = data.groupby(['year', 'month']).mean().reset_index()
