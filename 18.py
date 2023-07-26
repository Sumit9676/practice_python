# Demostrating the use of enumerate
# enumerate(iterable, start=0)
cars = ["Audi", "BMW", "Mercedes", "Toyota"]
for x in enumerate(cars):      # Type 1
    print(x)

print()
for x in enumerate(cars, start=1):  # Type 2
    print(x)

print()
for x in enumerate(cars, 10):        # Type 3
    print(x)

print()
print(list(enumerate(cars)))        # Type 4