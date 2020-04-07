# -*- coding:utf-8 -*-

"""Logic of gcd game."""

from random import randint

RULES = 'Find the greatest common divisor of given numbers.'


def find_gcd(first_number: int, second_number: int) -> int:
    """Find gcd."""
    if second_number == 0:
        return first_number
    return find_gcd(
        second_number,
        first_number % second_number,  # noqa: S001
    )


def create_round_parameters() -> tuple:
    """Create and return round question and right answer for gdc game."""
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    question = '{0} {1}'.format(str(first_number), str(second_number))
    return question, find_gcd(
        first_number,
        second_number,
    )
