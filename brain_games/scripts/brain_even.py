#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Module is being developed. Even game start."""

from brain_games.cli import show_even_rules, show_start_message
from brain_games.games.even import play_even


def main() -> None:
    """Start game."""
    show_start_message()
    show_even_rules()
    play_even()


if __name__ == '__main__':
    main()
