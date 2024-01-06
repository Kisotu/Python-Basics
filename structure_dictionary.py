# Dict - Ordered collection of items in key : value pairs.
capital_cities = {"Kenya": "Nairobi", "Tanzania": "Dodoma", "Uganda": "Kampala", "USA": "Washington DC", "UK": "London"}

# Prints cities
for cities in capital_cities.values():
    print(cities)

# Prints Countries
for countries in capital_cities.keys():
    print(countries)


print(capital_cities)

print(capital_cities["Kenya"])
print(capital_cities["Uganda"])
