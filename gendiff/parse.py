import json
import yaml


def parse(data, format):
    if format == 'json':
        return json.loads(data)
    elif format == 'yml' or format == 'yaml':
        return yaml.safe_load(data)
