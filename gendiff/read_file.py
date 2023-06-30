import os


def read_file(file_path):
    format = os.path.splitext(file_path)[-1].lstrip('.')
    with open(file_path) as file:
        text = file.read()
        return text, format
