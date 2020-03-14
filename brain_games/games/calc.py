# -*- coding:utf-8 -*-

"""Module is being developed. Logic of calc game."""

from random import randint

from brain_games.cli import ask_question, take_int_answer
from brain_games.game import play_game


def find_calc(first_number: int, second_number: int, operation_int: int) -> int:  # noqa: E501
    """Find operation result.

    # noqa: DAR101
    # noqa: DAR201

    """
    if operation_int == 1:
        correct_answer = first_number + second_number
    elif operation_int == 2:
        correct_answer = first_number - second_number
    else:
        correct_answer = first_number * second_number
    return correct_answer  # noqa: WPS331


def realise_calc_question() -> str:  # noqa: WPS210
    """Realise operation result.

    # noqa: DAR201

    """
    first_number = randint(1, 100)  # noqa: S311
    second_number = randint(1, 100)  # noqa: S311
    operation_int = randint(1, 3)  # noqa: S311
    if operation_int == 1:
        operator = '+'
    elif operation_int == 2:
        operator = '-'
    else:
        operator = '*'
    phrase = '{0} {1} {2}'.format(str(first_number), operator, str(second_number))  # noqa: E501
    ask_question(phrase)
    correct_answer = find_calc(first_number, second_number, operation_int)
    return str(correct_answer)  # noqa: WPS331


def play_calc() -> None:
    """Play calc game."""
    play_game(realise_calc_question, take_int_answer)
