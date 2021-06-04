# Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong,
# and then responds with a message accordingly.

from random import randint

keyWord = 'y'
while keyWord.lower() == 'y':
    # генерируем переменную для математической операции
    mathSign_1 = randint(0, 1)  # 0 - деление, 1 - умножение
    mathSign_2 = randint(0, 1)  # 0 - вычитание, 1 = сложение

    number_1 = randint(1000, 10001)
    number_2 = randint(2, 5)
    number_3 = randint(1, 200)

    counter_of_attempts = 3
    while counter_of_attempts != 0:
        print('Type in the answer for the following mathematical expression (must be rounded of): ')
        # производим математические расчеты и вывод выражения
        # в зависимости от сгенерированных ранее "математических знаков"
        if mathSign_1 == 0:
            result = number_1 / number_2
            if mathSign_2 == 0:
                result -= number_3
                print(f'{number_1} / {number_2} - {number_3}')
            else:
                result += number_3
                print(f'{number_1} / {number_2} + {number_3}')
        else:
            result = number_1 * number_2
            if mathSign_2 == 0:
                result -= number_3
                print(f'{number_1} * {number_2} - {number_3}')
            else:
                result += number_3
                print(f'{number_1} * {number_2} + {number_3}')

        # блок с вводом данных пользователем
        while True:
            answer = input('Answer: ')
            if not answer.isdigit():
                print('Invalid number!')
                continue
            answer = int(answer)
            break

        # блок с проверкой введенных данных
        if answer == round(result):
            print('You are right!')
            break
        else:
            counter_of_attempts -= 1
            print(f'Incorrect answer. You have {counter_of_attempts} more attempts')
    keyWord = input('Would you like to play again? (y - yes, n - no): ')
