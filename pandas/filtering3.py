# Import cars data
import pandas as pd
cars = pd.read_csv('../cars.csv', index_col = 0)


import numpy as np

cpc = cars['cars_per_cap']
# between = np.logical_and(cpc > 100, cpc< 500)
# medium = cars[between]

medium = cars[np.logical_and(cpc > 100, cpc < 500)]
print(medium)

