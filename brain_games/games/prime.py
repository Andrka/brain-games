# -*- coding:utf-8 -*-

"""Logic of prime game."""

from random import randint

RULES = ''.join((
    'Answer "yes" if given number is prime. ',
    'Otherwise answer "no".',
))


def check_if_prime(number: int) -> str:
    """Check number for prime."""
    if number % 2 == 0:
        if number == 2:
            return 'yes'
        return 'no'
    divisor = 3
    while divisor ** 2 <= number and number % divisor != 0:  # noqa: S001
        divisor += 2
    if divisor ** 2 > number:
        return 'yes'
    return 'no'


def create_round_parameters() -> tuple:
    """Create and return round question and right answer for prime game."""
    number = randint(1, 1000)
    return str(number), check_if_prime(number)
