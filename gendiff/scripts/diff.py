#!/usr/bin/env python3
from gendiff.user import User


def main():
    """Run an example code."""
    # it is ok to have some magical numbers locally
    print(User(name='Bob', age=42).get_introduction())  # noqa:WPS432


if __name__ == '__main__':
    main()
