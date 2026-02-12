# Tafheem Khan 30219735
# DATA 221 Assignment_2 Question 6 "Crime Risk vs Unemployment"
# I need to load crime.csv
# create a column risk:
# - HighCrime if ViolentCrimesPerPop >= 0.50
# - LowCrime otherwise
# then group by risk and compute average PctUnemployed
# then print results clearly

import pandas as pd
import numpy as np

DataFrame = pd.read_csv("crime.csv")

DataFrame["risk"] = np.where(
    DataFrame["ViolentCrimesPerPop"] >= 0.50,
    "HighCrime",
    "LowCrime"
)

AverageUnemployment = DataFrame.groupby("risk")["PctUnemployed"].mean()

print("Average unemployment (PctUnemployed) by risk group:")
for RiskGroup, AvgValue in AverageUnemployment.items():
    print(f"{RiskGroup}: {AvgValue:.4f}")
