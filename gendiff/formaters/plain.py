def plain_template(PROPERTY, key, symbol):
    return f'{PROPERTY} {key} {symbol}'


REMOVED = 'removed'
ADDED = 'added'
UNCHANGED = 'unchanged'
NESTED = 'nested'
CHANGED = 'changed'

PROPERTY = 'Property'

symbols_dict = {
                ADDED: f"{'was added with value'}: {'[complex value]'}",
                REMOVED: f"{'was removed'}",
                CHANGED: f"{'was updated. From'}",
                UNCHANGED: ""
                }


def plain(obj_dict):
    result = []
    for k, v in obj_dict.items():
        types = v.get('type')
        value = v.get('value')
        children = v.get('children')

        if types == UNCHANGED or types == ADDED or types == REMOVED:
            result.append(
                plain_template(PROPERTY, k, symbols_dict[types]))

        elif types == CHANGED:
            result.append(
                plain_template(
                    PROPERTY, k, f"{symbols_dict[CHANGED]} "
                                 f"'{value.get('old_value')}' "
                                 f"{'to'} '{value.get('new_value')}'"))

        else:
            result.append(
                plain_template(PROPERTY, k, f"{symbols_dict[UNCHANGED]} {plain(children)}")
            )

    result = '\n'.join(result)
    return result


# obj_dict = {
#     'follow': {
#         'type': 'removed',
#         'value': False,
#         'children': None
#     },
#     'host': {
#         'type': 'unchanged',
#         'value': 'hexlet.io',
#         'children': None
#     },
#     'proxy': {
#         'type': 'removed',
#         'value': '123.234.53.22',
#         'children': None
#     },
#     'timeout': {
#         'type': 'changed',
#         'value': {
#             'old_value': 50,
#             'new_value': 20
#         },
#         'children': None
#     },
#     'verbose': {
#         'type': 'added',
#         'value': True,
#         'children': None}
# }

# print(plain(obj_dict))
