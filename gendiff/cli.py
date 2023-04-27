import argparse


def parse_args():
    parser = argparse.ArgumentParser(
                        prog='gendiff',
                        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')           # positional argument
    parser.add_argument('second_file')      # option that takes a value
    parser.add_argument('-f FORMAT', '--format FORMAT',  help='set format of output', action='store_true')  # on/off flag
    return parser.parse_args()


def generate_diff():
    print('12')