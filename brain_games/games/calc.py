# -*- coding:utf-8 -*-

"""Logic of calc game."""

from random import randint

RULES = 'What is the result of the expression?'


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


def create_round_parameters() -> tuple:
    """Create and return round question and right answer for calc game."""
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    operation_int = randint(1, 3)
    if operation_int == 1:
        operator = '+'
    elif operation_int == 2:
        operator = '-'
    else:
        operator = '*'
    question = '{0} {1} {2}'.format(
        str(first_number),
        operator,
        str(second_number),
    )
    return question, find_calculation_result(
        first_number,
        second_number,
        operation_int,
    )
