from gendiff.constants import REMOVED, ADDED, UNCHANGED, NESTED, CHANGED


def create_diff_get(path_1, path_2):
    result = dict()
    all_keys = sorted(path_1.keys() | path_2.keys())

    for key in all_keys:
        if key not in path_2:
            result[key] = {
                'type': REMOVED,
                'value': path_1[key],
                'children': None
            }

        elif key not in path_1:
            result[key] = {
                'type': ADDED,
                'value': path_2[key],
                'children': None
            }

        elif path_1[key] == path_2[key]:
            result[key] = {
                'type': UNCHANGED,
                'value': path_1[key],
                'children': None
            }

        elif isinstance(path_1[key], dict) and isinstance(path_2[key], dict):
            result[key] = {
                'type': NESTED,
                'value': None,
                'children': create_diff_get(path_1[key], path_2[key])
            }

        else:
            result[key] = {
                'type': CHANGED,
                'value': {
                    'old_value': path_1[key],
                    'new_value': path_2[key]
                },
                'children': None
            }

    return result
