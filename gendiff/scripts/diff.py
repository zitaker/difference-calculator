#!/usr/bin/env python3
from gendiff.cli import parse_args
from gendiff import generate_diff


def main():
    parse_args()
    diff = generate_diff(file_path1, file_path2)
    print(diff)



if __name__ == '__main__':
    main()
