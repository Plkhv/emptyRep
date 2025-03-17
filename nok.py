"""Игра 'НОК'."""
import random as r
import math

def generate_question(name):
    """Функция генерации вопросов."""
    flag = 0
    while flag != 3:
        a, b, c = r.randint(1,20), r.randint(1,20), r.randint(1,20)
        print(f'Question: {a} {b} {c}')

        def lcm_two(x, y):
            return abs(x * y) // math.gcd(x, y)

        nok = lcm_two(lcm_two(a, b), c)
        answer_nok = int(input('Your answer: '))
        if nok == answer_nok:
            print('Correct!')
            flag += 1
        else:
            print(f"'{answer_nok}' is wrong answer ;(. Correct answer was '{nok}'.")
            print(f"Let's try again, {name}!")
            flag = 0

print('\nWelcome to the Brain Games!')
name = input('May I have your name? ')
print(f'Hello, {name}!\nFind the smallest common multiple of given numbers.')
generate_question(name)
print(f"Congratulations, {name}!")