import json
import yaml


def file_parser(path):
    open_path = open(path)
    if path.endswith('.yaml') or path.endswith('.yml'):
        return yaml.load(open_path, Loader=yaml.FullLoader)
    elif path.endswith('.json'):
        return json.loads(open_path.read())
