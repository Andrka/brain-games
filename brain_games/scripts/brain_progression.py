#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Module is being developed. Progression game start."""

from brain_games.cli import font_bold, font_end
from brain_games.games.progression import play_progression


def main() -> None:
    """Start game."""
    print('Welcome to the Brain Games!')  # noqa: T001
    print('What number is missing {0}in{1} the progression?'.format(font_bold, font_end))  # noqa: T001, E501
    play_progression()


if __name__ == '__main__':
    main()
