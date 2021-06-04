# Create a program that reads an input string and then creates and prints 5 random strings
# from characters of the input string.
# For example, the program obtained the word ‘hello’, so it should print 5 random strings(words)
# that combine characters ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …
# Tips: Use random module to get random char from string)

from random import shuffle, sample

# 1 способ
answer = input('Type in your string: ')
string_list = list(answer)

counter = 0
while counter != 5:
    shuffle(string_list)
    print(''.join(string_list))
    counter += 1

# 2 способ
answer = input('Type in your string: ')
string_list = list(answer)

counter = 0
while counter != 5:
    print(''.join(sample(string_list, len(answer))))
    counter += 1
