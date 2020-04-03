# -*- coding:utf-8 -*-

"""Logic of even game."""

from random import randint

from brain_games.cli import ask_question, take_str_answer
from brain_games.game import play_game


def check_if_even(quiz_number: int) -> str:
    """Check number for even."""
    if quiz_number % 2 == 0:
        return 'yes'
    return 'no'


def create_even_question() -> str:
    """Create, show to user number and return if it is even."""
    quiz_number = randint(1, 100)
    phrase = '{0}'.format(str(quiz_number))
    ask_question(phrase)
    return check_if_even(quiz_number)


def play_even(user_name: str = ''):
    """Play even game."""
    play_game(create_even_question, take_str_answer, user_name)
