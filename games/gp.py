"""Игра 'Геометрическая прогрессия'."""
import sys
sys.path.append('..')

from main_game import greetings, outro
import random as r

name = greetings()

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
gp_generate_question(name)

outro(name)
