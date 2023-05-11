#!/usr/bin/env python3
from gendiff.cli import parse_args
from gendiff.generate_diff import diff_generate


def main():
    args = parse_args()
    diff = diff_generate(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
