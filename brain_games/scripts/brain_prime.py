#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Module is being developed. Prime game start."""

from brain_games.cli import show_prime_rules, show_start_message
from brain_games.games.prime import play_prime


def main() -> None:
    """Start game."""
    show_start_message()
    show_prime_rules()
    play_prime()


if __name__ == '__main__':
    main()
