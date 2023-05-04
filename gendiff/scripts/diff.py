#!/usr/bin/env python3
from gendiff.cli import parse_args
from gendiff.generate_diff import diff_generate


def main():
    # parse_args()
    args = parse_args()
    diff = diff_generate(args.file1_json.json, args.file2_json.json)
    print(diff)


if __name__ == '__main__':
    main()
