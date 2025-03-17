"""Игра 'Геометрическая прогрессия'."""
from ..main_game import gp_generate_question, greetings, outro
import random as r

name = greetings()

gp_generate_question(name)

outro(name)