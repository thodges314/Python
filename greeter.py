# name = input("Please enter your name: ")
# print("Hello, " + name.title() + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt).title()

print("Hello, " + name + "!")