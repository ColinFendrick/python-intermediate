import pandas as pd
import time

df = pd.DataFrame(
    data={'Values': range(1, 100000)}
)
print(df.head())
print(df.shape)

start_time_iterrows = time.time()

summed_iterrows = 0
for _, r in df.iterrows():
    summed_iterrows += r['Values']

print(summed_iterrows)
print("Iterrows took:", time.time() - start_time_iterrows)

start_time_itertuples = time.time()
summed_itertuples = 0
for r in df.itertuples(index=False):
    summed_itertuples += r.Values

print(summed_itertuples)
print('Itertuples took:', time.time() - start_time_itertuples)
