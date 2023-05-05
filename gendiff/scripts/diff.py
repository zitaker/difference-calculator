#!/usr/bin/env python3
from gendiff.cli import parse_args
from gendiff.generate_diff import diff_generate


def main():
    # parse_args()
    args = parse_args()
    # diff = diff_generate(args.file1_json.json, args.file2_json.json)
    diff = diff_generate(args.first_file, args.second_file)
    # diff = diff_generate(args.file1, args.file2)
    print(diff)


if __name__ == '__main__':
    main()
