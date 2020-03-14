# -*- coding:utf-8 -*-

"""Module is being developed. Logic of progression game."""

from random import randint

from brain_games.cli import ask_question, take_int_answer
from brain_games.game import play_game


def find_progression(start_number: int, step_number: int, miss_number: int) -> int:  # noqa: E501
    """Find progression.

    # noqa: DAR101
    # noqa: DAR201

    """
    return start_number + (miss_number - 1) * step_number


def realise_progression_question() -> str:  # noqa: WPS210
    """Realise progression.

    # noqa: DAR201

    """
    start_number = randint(1, 10)  # noqa: S311
    step_number = randint(1, 10)  # noqa: S311
    miss_number = randint(1, 10)  # noqa: S311
    phrase = ''
    for index in range(10):
        if (index + 1) == miss_number:
            phrase += '..'  # noqa: WPS336
        else:
            phrase += str(start_number + index * step_number)  # noqa: WPS336
        if index < 9:
            phrase += ' '  # noqa: WPS336
    ask_question(phrase)
    correct_answer = find_progression(start_number, step_number, miss_number)
    return str(correct_answer)


def play_progression() -> None:
    """Play progression game."""
    play_game(realise_progression_question, take_int_answer)
