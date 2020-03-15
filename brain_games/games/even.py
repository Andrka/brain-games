# -*- coding:utf-8 -*-

"""Module is being developed. Logic of even game."""

from random import randint

from brain_games.cli import ask_question, take_str_answer
from brain_games.game import play_game


def check_even(quiz_number: int) -> str:
    """Check number for even.

    # noqa: DAR101
    # noqa: DAR201

    """
    if quiz_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer  # noqa: WPS331


def realise_even_question() -> str:
    """Realise number type.

    # noqa: DAR201

    """
    quiz_number = randint(1, 100)  # noqa: S311
    phrase = '{0}'.format(str(quiz_number))
    ask_question(phrase)
    correct_answer = check_even(quiz_number)
    return correct_answer  # noqa: WPS331


def play_even(name: str = '') -> None:
    """Play even game.

    # noqa: DAR101

    """
    play_game(realise_even_question, take_str_answer, name)
