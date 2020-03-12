# -*- coding:utf-8 -*-

"""Module is being developed. Command line interface."""

import prompt

font_red = '\033[91m'
font_blue = '\033[96m'
font_bold = '\033[1m'
font_end = '\033[0m'


def take_name() -> str:
    """Take user name.

    # noqa: DAR201

    """
    return prompt.string('May I have your name? ')


def welcome_user() -> None:
    """Greet user by name."""
    print('Hello, {0}!'.format(take_name()))  # noqa: T001


def take_answer() -> str:
    """Take answer from user.

    # noqa: DAR201

    """
    return prompt.string('Your answer: ')
