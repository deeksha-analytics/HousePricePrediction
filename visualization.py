import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("housing.csv")

plt.figure(figsize=(8,5))

plt.scatter(
    df["MedInc"],
    df["Price"]
)

plt.xlabel("Median Income")
plt.ylabel("Price")

plt.title("Income vs House Price")

plt.show()