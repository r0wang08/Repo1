import pandas as pd

df = pd.read_csv('amazon.csv')
print(df.head())
print(df.info())

print(df.isnull().sum())

df = df.dropna()

#check if null values are dropped
print(df.isnull().sum())
print(df.head())


df = pd.read_csv('amazon.csv')
print(df.head())

