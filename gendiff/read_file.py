import os


def read_file(path):
    format = os.path.splitext(path)[-1].lstrip('.')
    with open(path) as file:
        text = file.read()
        return text, format
