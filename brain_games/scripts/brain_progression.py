#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Module is being developed. Progression game start."""

from brain_games.cli import show_progression_rules, show_start_message
from brain_games.games.progression import play_progression


def main() -> None:
    """Start game."""
    show_start_message()
    show_progression_rules()
    play_progression()


if __name__ == '__main__':
    main()
