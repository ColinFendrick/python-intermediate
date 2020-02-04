# Dictionary of dictionaries
europe = {'spain': {'capital': 'madrid', 'population': 46.77},
          'france': {'capital': 'paris', 'population': 66.03},
          'germany': {'capital': 'berlin', 'population': 80.62},
          'norway': {'capital': 'oslo', 'population': 5.084}}
print(europe['france']['capital'])

italy = {'capital': 'rome', 'population': 59.83}

europe['italy'] = italy

print(europe)
