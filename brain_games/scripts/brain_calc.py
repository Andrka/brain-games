#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Module is being developed. Calc game start."""

from brain_games.cli import show_calc_rules, show_start_message
from brain_games.games.calc import play_calc


def main() -> None:
    """Start game."""
    show_start_message()
    show_calc_rules()
    play_calc()


if __name__ == '__main__':
    main()
