# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('../cars.csv', index_col=0)
print(cars)
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])

# Print out locations and index locations
print(cars.loc[22])
print(cars.iloc[22])
# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap', 'drives_right']])
