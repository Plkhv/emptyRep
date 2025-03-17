from .games.gp import gp_generate_question
from .games.nok import nok_generate_question
import random as r
import math

def greetings():
    print('\nWelcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!\nFind the smallest common multiple of given numbers.')
    return name

def outro(name):
    print(f"Congratulations, {name}!")

def nok_generate_question(name):
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


def gp_generate_question(name):
    """Функция генерации вопросов."""
    flag = 0
    while flag != 3:
        a, b, c = r.randint(1,5), r.randint(1,10), r.randint(5,10)

        def geometric_progression(a, r, n):
            return [a * r**i for i in range(n)]

        rand = r.randint(0,c-1)
        progression = geometric_progression(a,b,c)
        gp = progression[rand]
        progression[rand] = '..'
        print(f'Question: {progression}')
        answer_gp = int(input('Your answer: '))
        if gp == answer_gp:
            print('Correct!')
            flag += 1
        else:
            print(f"'{answer_gp}' is wrong answer ;(. Correct answer was '{gp}'.")
            print(f"Let's try again, {name}!")
            flag = 0