favourite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python'
}

# print("Sarah's favourite language is " + favourite_languages['sarah'].title() + '.')
for name, language in favourite_languages.items():
	print(name.title() + "'s favourite language is " + language.title() + ".")

# these two work the same way
print('\nnames: ')
for name in favourite_languages.keys():
	print(name.title())

print('\nnames: ')
for name in favourite_languages:	# keys is the default
	print(name.title())

print('\n')
# use that differnetly
friends = ['phil', 'sarah']
for name in favourite_languages.keys():
	print(name.title())

	if name in friends:
		print(" Hi " + name.title() + ", I see that your favourite langaue is " +
			favourite_languages[name].title() + "!")

print("****************************")
# in order
for name in sorted(favourite_languages.keys()):
	print(name.title() + ", thank you for taking this poll.")

print("****************************")
# loop through values - repeats
print("The following languages have been mentioned:")
for language in favourite_languages.values():
	print(language.title())

print("****************************")
# loop through values - set for no repeats
print("The following languages have been mentioned:")
for language in set(favourite_languages.values()):
	print(language.title())