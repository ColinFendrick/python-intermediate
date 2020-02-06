import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50]) 
your_house = np.array([14.0, 24.0, 14.25, 9.0])

print(my_house >= 18)  # [ True  True False False]

print(my_house < your_house) # [False True True True]
