#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Module is being developed. Gcd game start."""

from brain_games.games.gcd import play_gcd


def main() -> None:
    """Start game."""
    print('Welcome to the Brain Games!')  # noqa: T001
    print('Find the greatest common divisor of given numbers.')  # noqa: T001
    play_gcd()


if __name__ == '__main__':
    main()
