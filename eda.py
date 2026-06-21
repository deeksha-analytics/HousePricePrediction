import pandas as pd

# Load dataset
df = pd.read_csv("housing.csv")

# First 5 rows
print(df.head())

# Dataset shape
print("\nShape:")
print(df.shape)

# Column names
print("\nColumns:")
print(df.columns)

# Dataset information
print("\nInfo:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistics:")
print(df.describe())