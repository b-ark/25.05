# Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement

while True:
    name = input('Type in your name: ')
    if name.isalpha():
        break

while True:
    age = input('Type in your age: ')
    if age.isdigit():
        break

print(f'Hello {name.title()}, on your next birthday you’ll be {int(age)+1} years')
