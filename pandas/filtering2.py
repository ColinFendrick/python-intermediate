# Import cars data
import pandas as pd
cars = pd.read_csv('../cars.csv', index_col=0)

# cpc = cars['cars_per_cap']
# many_cars = cpc > 500
# car_maniac = cars[many_cars]

car_maniac = cars[cars['cars_per_cap'] > 500]

print(car_maniac)
