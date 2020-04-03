#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Even game start."""

from brain_games.cli import print_even_rules, print_start_message
from brain_games.games.even import play_even


def main():
    """Start game."""
    print_start_message()
    print_even_rules()
    play_even()


if __name__ == '__main__':
    main()
