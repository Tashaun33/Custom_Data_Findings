
import pandas as pd
import requests
from io import StringIO

# Function to download CSV from a URL and load into a dataframe
def load_csv_from_url(url):
    response = requests.get(url)
    response.raise_for_status()
    return pd.read_csv(StringIO(response.text))

# 1. Dirty Dataset (Kaggle alternative, hosted CSV)
dirty_url = "https://raw.githubusercontent.com/amruthayenikonda/dirty-dataset-to-practice-data-cleaning/main/dirty_data.csv"
dirty_df = load_csv_from_url(dirty_url)

# 2. FiveThirtyEight - College Majors
majors_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv"
majors_df = load_csv_from_url(majors_url)

# 3. FiveThirtyEight - US Weather History (one city's file)
weather_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/us-weather-history/KCLT.csv"
weather_df = load_csv_from_url(weather_url)

# Show previews
print("\n--- Dirty Dataset ---")
print(dirty_df.head())
print(dirty_df.info())

print("\n--- College Majors Dataset ---")
print(majors_df.head())
print(majors_df.info())

print("\n--- US Weather History (Charlotte) ---")
print(weather_df.head())
print(weather_df.info())

import messy_data_loader as mdl 
pd = mdl.load_dirty_dataset()   
pd.head()   
