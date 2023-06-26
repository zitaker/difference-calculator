from gendiff.constants import REMOVED, ADDED, UNCHANGED, NESTED, CHANGED


def create_diff_get(old_data, new_data):
    result = dict()
    all_keys = sorted(old_data.keys() | new_data.keys())

    for key in all_keys:
        if key not in new_data:
            result[key] = {
                'type': REMOVED,
                'value': old_data[key],
                'children': None
            }

        elif key not in old_data:
            result[key] = {
                'type': ADDED,
                'value': new_data[key],
                'children': None
            }

        elif old_data[key] == new_data[key]:
            result[key] = {
                'type': UNCHANGED,
                'value': old_data[key],
                'children': None
            }

        elif isinstance(old_data[key], dict) and \
                isinstance(new_data[key], dict):
            result[key] = {
                'type': NESTED,
                'value': None,
                'children': create_diff_get(old_data[key], new_data[key])
            }

        else:
            result[key] = {
                'type': CHANGED,
                'value': {
                    'old_value': old_data[key],
                    'new_value': new_data[key]
                },
                'children': None
            }

    return result
