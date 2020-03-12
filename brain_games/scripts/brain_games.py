# -*- coding:utf-8 -*-

"""Module is being developed. General script."""

from brain_games.cli import welcome_user


def main() -> None:
    """Start application."""
    print('Welcome to the Brain Games!')  # noqa: T001
    print('')  # noqa: T001
    welcome_user()


if __name__ == '__main__':
    main()
