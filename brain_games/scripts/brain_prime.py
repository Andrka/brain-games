#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Prime game start."""

from brain_games.cli import print_prime_rules, print_start_message
from brain_games.games.prime import play_prime


def main():
    """Start game."""
    print_start_message()
    print_prime_rules()
    play_prime()


if __name__ == '__main__':
    main()
