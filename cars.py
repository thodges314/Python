cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse = True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print ("\nHere is the sorted list:")
print(sorted(cars))

print("Here is the original list again:")
print(cars)

cars.reverse()
print("Here is the original list backwards:")
print(cars)

print("The length of the list is " + str(len(cars)) + ".")