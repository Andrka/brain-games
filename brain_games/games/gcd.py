# -*- coding:utf-8 -*-

"""Module is being developed. Logic of gcd game."""

from random import randint

from brain_games.cli import ask_question, take_int_answer
from brain_games.game import play_game


def find_gcd(first_number: int, second_number: int) -> int:
    """Find gcd.

    # noqa: DAR101
    # noqa: DAR201

    """
    if second_number == 0:
        return first_number
    else:
        return find_gcd(second_number, first_number % second_number)  # noqa: WPS503, S001, E501


def realise_gcd_question() -> str:  # noqa: WPS210
    """Realise gcd.

    # noqa: DAR201

    """
    first_number = randint(1, 100)  # noqa: S311
    second_number = randint(1, 100)  # noqa: S311
    phrase = '{0} {1}'.format(str(first_number), str(second_number))
    ask_question(phrase)
    correct_answer = find_gcd(first_number, second_number)
    return str(correct_answer)  # noqa: WPS331


def play_gcd(name: str = '') -> None:
    """Play gcd game.

    # noqa: DAR101

    """
    play_game(realise_gcd_question, take_int_answer, name)
