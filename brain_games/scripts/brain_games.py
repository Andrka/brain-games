#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""General script - game selecting."""

from brain_games.cli import print_start_message, take_user_name


def main():
    """Start application."""
    print_start_message()
    take_user_name()


if __name__ == '__main__':
    main()
