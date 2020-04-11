# -*- coding:utf-8 -*-

"""Logic of prime game."""

from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int) -> bool:
    """Check number for prime."""
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    divisor = 3
    while divisor ** 2 <= number and number % divisor != 0:  # noqa: S001
        divisor += 2
    if divisor ** 2 > number:
        return True
    return False


def create_game_parameters() -> tuple:
    """Create and return question and right answer for prime game."""
    number = randint(1, 1000)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return str(number), correct_answer
