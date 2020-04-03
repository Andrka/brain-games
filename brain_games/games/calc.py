# -*- coding:utf-8 -*-

"""Logic of calc game."""

from random import randint

from brain_games.cli import ask_question, take_int_answer
from brain_games.game import play_game


def find_calculation_result(
    first_number: int,
    second_number: int,
    operation_int: int,
) -> int:
    """Find operation result."""
    if operation_int == 1:
        return first_number + second_number
    if operation_int == 2:
        return first_number - second_number
    return first_number * second_number


def create_calc_question() -> str:
    """Create, show to user calc question and return it's answer."""
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    operation_int = randint(1, 3)
    if operation_int == 1:
        operator = '+'
    elif operation_int == 2:
        operator = '-'
    else:
        operator = '*'
    phrase = '{0} {1} {2}'.format(
        str(first_number),
        operator,
        str(second_number),
    )
    ask_question(phrase)
    return str(find_calculation_result(
        first_number,
        second_number,
        operation_int,
    ))


def play_calc(user_name: str = ''):
    """Play calc game."""
    play_game(create_calc_question, take_int_answer, user_name)
