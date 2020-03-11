# -*- coding:utf-8 -*-

"""Module is being developed. Command line interface."""
import prompt


def welcome_user():
    """Greet user by name."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))  # noqa: T001
