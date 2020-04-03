#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Progression game start."""

from brain_games.cli import print_progression_rules, print_start_message
from brain_games.games.progression import play_progression


def main():
    """Start game."""
    print_start_message()
    print_progression_rules()
    play_progression()


if __name__ == '__main__':
    main()
