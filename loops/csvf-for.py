# Import cars data
import pandas as pd
import numpy as py
cars = pd.read_csv('cars.csv', index_col=0)

# Adapt for loop
for lab, row in cars.iterrows():
    print(
        lab + ": " + str(row['cars_per_cap'])
    )
