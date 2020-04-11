# -*- coding:utf-8 -*-

"""Logic of gcd game."""

from random import randint

RULES = 'Find the greatest common divisor of given numbers.'


def find_gcd(first_number: int, second_number: int) -> int:
    """Find gcd."""
    while second_number != 0:
        first_number, second_number = (
            second_number,
            first_number % second_number,  # noqa: S001
        )
    return first_number


def create_game_parameters() -> tuple:
    """Create and return question and right answer for gdc game."""
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    question = '{0} {1}'.format(first_number, second_number)
    return question, str(find_gcd(first_number, second_number))
