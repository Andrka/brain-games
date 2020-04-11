# -*- coding:utf-8 -*-

"""Logic of calc game."""

from operator import add, mul, sub
from random import choice, randint

RULES = 'What is the result of the expression?'
OPERATIONS = (('+', add), ('-', sub), ('*', mul))


def create_game_parameters() -> tuple:
    """Create and return question and right answer for calc game."""
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    symbol, operation = choice(OPERATIONS)
    question = '{0} {1} {2}'.format(
        first_number,
        symbol,
        second_number,
    )
    return question, str(operation(
        first_number,
        second_number,
    ))
