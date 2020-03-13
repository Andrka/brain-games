# -*- coding:utf-8 -*-

"""Module is being developed. Calc game start."""

from brain_games.games.calc import play_calc


def main() -> None:
    """Start game."""
    print('Welcome to the Brain Games!')  # noqa: T001
    print('What is the result of the exspression?')  # noqa: T001
    play_calc()


if __name__ == '__main__':
    main()
