# ##dictionary intro
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])

# new_points = alien_0['points']
# print("you just earned " + str(new_points) + " points.")

# alien_0['x_position'] = 0
# alien_0['y position'] = 25
# print(alien_0)

# ## build and modify dictionary
# alien_0 = {}

# alien_0['color'] = 'green'
# alien_0['points'] = 5

# print(alien_0)

# print("The alien is "+ alien_0['color'] + ".")

# alien_0['color'] = 'yellow'
# print("The alien is "+ alien_0['color'] + ".")

## track position
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium', 'points' : 100}
print("Original x position: " + str(alien_0['x_position']))
# move alien to the right based on it's speed
if alien_0['speed'] == 'slow' :
	x_increment = 1
elif alien_0['speed'] == 'medium' :
	x_increment = 2
else:
	x_increment = 3

# new position is old position plus increments
alien_0['x_position'] += x_increment

print("New x position: " + str(alien_0['x_position']))

## delete key
print(alien_0)

del alien_0['points']
print(alien_0)