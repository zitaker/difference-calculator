def plain_template(PROPERTY, key, symbol):
    return f'{PROPERTY} {key} {symbol}'

def plain_template_2(PRINT, key, symbol):
    return f'{PRINT} {key} {symbol}'


REMOVED = 'removed'
ADDED = 'added'
UNCHANGED = 'unchanged'
NESTED = 'nested'
CHANGED = 'changed'

PROPERTY = 'Property'
PRINT = '.'

symbols_dict = {
                ADDED: f"{'was added with value'}: {'[complex value]'}",
                REMOVED: f"{'was removed'}",
                CHANGED: f"{'was updated. From'}",
                UNCHANGED: f"{''}:"
                }

# symbols_dict_2 = {
#                 ADDED: f"{'was added with value'}: {'VALUE'}",
#                 REMOVED: f"{'was removed'}",
#                 CHANGED: f"{'was updated. From'}",
#                 UNCHANGED: f"{'was added with value'}:"
#                 }


def one_plain(obj_dict):
    result = []
    for k, v in obj_dict.items():
        types = v.get('type')
        value = v.get('value')

        if types == ADDED or types == REMOVED:
            result.append(
                plain_template(PROPERTY, k, symbols_dict[types]))

        elif types == CHANGED:
            result.append(
                plain_template(
                    PROPERTY, k, f"{symbols_dict[CHANGED]} "
                                 f"'{value.get('old_value')}' "
                                 f"{'to'} '{value.get('new_value')}'"))

    result = '\n'.join(result)
    return result


def two_plan(obj_dict):
    result = []
    for k, v in obj_dict.items():
        types = v.get('type')
        value = v.get('value')
        children = v.get('children')

        if types == UNCHANGED or types == ADDED or types == REMOVED:
            result.append(
                plain_template(PROPERTY, k, symbols_dict_2[types]))

        # elif types == CHANGED:
        #     result.append(
        #         plain_template(
        #             PROPERTY, k, f"{symbols_dict_2[CHANGED]} "
        #                          f"'{value.get('old_value')}' "
        #                          f"{'to'} '{value.get('new_value')}'"))

        # else:
        #     result.append(
        #         plain_template_2(PRINT, k, f"{symbols_dict_2[UNCHANGED]} {two_plan(children)}"))

        elif types == UNCHANGED:
            result.append(
                plain_template_2(PRINT, k, f"{symbols_dict_2[UNCHANGED]} {two_plan(value)}")
            )


    result = '\n'.join(result)
    return result

def plain(obj_dict):
    result = two_plan(obj_dict)
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
