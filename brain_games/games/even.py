# -*- coding:utf-8 -*-

"""Logic of even game."""

from random import randint

RULES = 'Answer "yes" if number is even otherwise answer "no".'


def is_even(number: int) -> bool:
    """Check number for even."""
    return number % 2 == 0


def create_game_parameters() -> tuple:
    """Create and return question and right answer for even game."""
    number = randint(1, 100)
    question = str(number)
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
