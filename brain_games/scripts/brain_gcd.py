#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Gcd game start."""

from brain_games.cli import print_gcd_rules, print_start_message
from brain_games.games.gcd import play_gcd


def main():
    """Start game."""
    print_start_message()
    print_gcd_rules()
    play_gcd()


if __name__ == '__main__':
    main()
