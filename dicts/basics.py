# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

ind_ger = countries.index('germany')

print(capitals[ind_ger])

europe = {'spain': 'madrid', 'france': 'paris',
          'germany': 'berlin', 'norway': 'oslo'}

print(europe)
print(europe.keys())
print(europe['norway'])
