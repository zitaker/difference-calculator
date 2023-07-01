import json
import yaml


def parse(data, path):
    if path.endswith('.json'):
        return json.loads(data)
    elif path.endswith('.yaml') or path.endswith('.yml'):
        return yaml.safe_load(data)
