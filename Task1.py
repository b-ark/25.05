#  Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
#  The result should be sent back to the user via a print statement.

from random import randrange

# суть идеи - у пользователя есть 3 попытки, чтобы угадать число. Вне зависимости от результата игры,
# пользователю будет предложено сыграть ещё раз
print('Hello! This is a guessing game! You have 3 attempts to guess the number from 1 to 10 inclusive!')
answer = 'y'
while answer.lower() == 'y':
    attempt = 0
    number = randrange(1, 11)
    while attempt != 3:
        guess = input('Type in your guess: ')

        # проверка на дурака
        if not guess.isdigit():
            print('Invalid number!')
            continue

        guess = int(guess)

        if guess == number:
            print('Congrats! You got the right number!')
            break
        elif guess < number:
            print('Unlucky! Your number is less than the guessed one')
        else:
            print('Unlucky! Your number is greater than the guessed one')

        attempt += 1

    if attempt == 3:
        print('You have ran out of attempts! The guessed number was', number)

    answer = input('Would you like to play again? (y - yes, n - no): ')
