motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('triumph')
print(motorcycles)

motorcycles.insert(1, 'harley davidson')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
print(motorcycles)

first_motorcycle = motorcycles.pop(0)
print('The first motorcycle that I owned was a ' + first_motorcycle.title() + '.')

motorcycles.remove('yamaha')
print(motorcycles)