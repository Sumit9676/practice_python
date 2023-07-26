# Different types of using iterators in Python
cars = ["Audi", "BMW", "Mercedes", "Toyota"] 
i = 0
while (i < len(cars)):             #Type 1
    print(cars[i], end = "  ")
    i += 1

print()
for x in cars:                     #Type 2
    print(x, end = "  ")           

print()
for a in range(len(cars)):         #Type 3
    print(cars[a], end = "  ")