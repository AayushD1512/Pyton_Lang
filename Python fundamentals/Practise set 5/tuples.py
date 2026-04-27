coordinates = (10,20)
a,b = coordinates
print(a, b)

# coordinates[0]=50

#convert tuple to a list then change first element and convert back to tuple
coordinates = list(coordinates)
coordinates[0] = 50
coordinates = tuple(coordinates)
print(coordinates)