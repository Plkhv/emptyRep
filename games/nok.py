"""Игра 'НОК'."""
from ..main_game import greetings, outro, nok_generate_question
import random as r
import math

name = greetings()

nok_generate_question(name)

outro(name)