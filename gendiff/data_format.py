import os.path


def data_format(path):
    format = os.path.splitext(path)[-1].lstrip('.')
    return format
