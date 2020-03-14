#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Module is being developed. Even game start."""

from brain_games.cli import font_blue, font_bold, font_end, font_red
from brain_games.games.even import play_even


def main() -> None:
    """Start game."""
    print('Welcome to the Brain Games!')  # noqa: T001
    print('Answer {0}"yes"{1} '.format(font_red, font_end), end='')  # noqa: T001, E501
    print('{0}if{1} number even otherwise '.format(font_bold, font_end), end='')  # noqa: T001, E501
    print('answer {0}"no"{1}{2}.{3}'.format(font_red, font_end, font_blue, font_end))  # noqa: T001, E501
    play_even()


if __name__ == '__main__':
    main()
