import argparse


parser = argparse.ArgumentParser(
                    prog='gendiff',
                    description='Compares two configuration files and shows a difference.')
parser.add_argument('first_file')           # positional argument
parser.add_argument('second_file')      # option that takes a value
parser.add_argument('-f FORMAT', '--format FORMAT',  help='set format of output', action='store_true')  # on/off flag
args = parser.parse_args()
print(args.filename)