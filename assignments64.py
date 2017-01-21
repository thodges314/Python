# #4.3
# for value in range(1, 21):
# 	print(value)

# #4.4
# for value in range(1, 1000001):
# 	print(value)

#4.5
millions = list(range(1,1000001))
print("First: " + str(min(millions)))
print("Last: " + str(max(millions)))
print("Sum: " + str(sum(millions)))

#4.6
odds = list(range(1, 20, 2))
for value in odds:
	print(value)

#4.7
threes = list(range(3,31,3))
for value in threes:
	print(value)

#4.7, 4.8
cubes = [value**3 for value in range(1,11)]
for cube in cubes:
	print(cube)