from sklearn.datasets import fetch_california_housing
import pandas as pd

housing = fetch_california_housing()

df = pd.DataFrame(
    housing.data,
    columns=housing.feature_names
)

df["Price"] = housing.target

# Save as CSV
df.to_csv("housing.csv", index=False)

print("Dataset saved successfully!")