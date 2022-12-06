import pandas as pd
dataset=pd.read_csv('city_day.csv')
dataset
dataset.isnull()
dataset.isnull().head(10)
dataset.isnull().sum()
dataset.isnull().head().sum()
modifieddataset=dataset.filla("")
modifieddataset.isnull().sum()

dataset=dataset.dropna()

