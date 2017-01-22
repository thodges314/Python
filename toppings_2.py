requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
	print("adding mushrooms")
if 'pepperoni' in requested_toppings:
	print("adding pepperoni")
if 'extra cheese' in requested_toppings:
	print("adding extra cheese")

print("\nFinished making your pizza!")

# with lists
print("\n************************************************************")
requested_toppings = ['mushrooms', 'extra cheese', 'green peppers', 2]

for requested_topping in requested_toppings:
	print("adding " + str(requested_topping) + ".")

print("\nFinished making your pizza!")

# with lists
print("\n************************************************************")
requested_toppings = ['mushrooms', 'extra cheese', 'green peppers', 2]

for requested_topping in requested_toppings:
	if str(requested_topping).lower() == 'green peppers':
		print("Sorry we are out of green peppers right now!")
	else:
		print("adding " + str(requested_topping) + ".")

print("\nFinished making your pizza!")

# check for empty
print("\n************************************************************")
requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		if str(requested_topping).lower() == 'green peppers':
			print("Sorry we are out of green peppers right now!")
		else:
			print("adding " + str(requested_topping) + ".")
	print("\nFinished making your pizza!")
else:
	print("are you sure that you want a plain pizza?")

# multiple lists
print("\n************************************************************")
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni',
						'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'extra cheese', 'french fries']

for requested_topping in requested_toppings:
	if str(requested_topping).lower() in available_toppings:
		print("adding " + str(requested_topping) + ".")
	else:
		print("sorry, we don't have " + requested_topping + '.')
print("\nFinished making your pizza!")