#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Module is being developed. Gcd game start."""

from brain_games.cli import show_gcd_rules, show_start_message
from brain_games.games.gcd import play_gcd


def main() -> None:
    """Start game."""
    show_start_message()
    show_gcd_rules()
    play_gcd()


if __name__ == '__main__':
    main()
