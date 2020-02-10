import numpy as np

# Starting step
step = 50

dice = np.random.randint(1, 7)

if dice <= 2:
    step = step - 1
elif 2 < dice < 6:
    step = step + 1
else:
    step = step + np.random.randint(1, 7)

# Print out dice and step
print(dice, step)
