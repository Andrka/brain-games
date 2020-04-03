#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Calc game start."""

from brain_games.cli import print_calc_rules, print_start_message
from brain_games.games.calc import play_calc


def main():
    """Start game."""
    print_start_message()
    print_calc_rules()
    play_calc()


if __name__ == '__main__':
    main()
