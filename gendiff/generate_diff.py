from gendiff.constants import PLUS, MINUS, SPASE
from gendiff.parser import file_parser


def create_diff_dict(dict_1, dict_2):
    diff_dict = dict()

    # если такая конструкция то сортирует по алфавиту, но пропадают значения
    for key, value in dict_1.items():
        diff_dict[key] = value

    for key, value in dict_2.items():
        diff_dict[key] = value

        """
        {
     common: {
       follow: False
       setting1: Value 1
       setting3: None
       setting4: blah blah
       setting5: {
         key5: value5
        }
       setting6: {
         key: value
         ops: vops
         doge: {
           wow: so much
          }
        }
      }
     group1: {
       foo: bar
       baz: bars
       nest: str
      }
     group2: {
       abc: 12345
       deep: {
         id: 45
        }
      }
     group3: {
       deep: {
         id: {
           number: 45
          }
        }
       fee: 100500
      }
    }
    
        """

    # пропадают значения, не по алфавиту, и после знака (~) - думает что
    # элементы все равны, даже если они отсутствуют в другом словаре, вывод:
    """
    {
        common: {
          + follow: false
            setting1: Value 1
          - setting2: 200
          - setting3: true
          + setting3: null
          + setting4: blah blah
          + setting5: {
                key5: value5
            }
            setting6: {
                doge: {
                  - wow:
                  + wow: so much
                }
                key: value
              + ops: vops
            }
        }
        group1: {
          - baz: bas
          + baz: bars
            foo: bar
          - nest: {
                key: value
            }
          + nest: str
        }
      - group2: {
            abc: 12345
            deep: {
                id: 45
            }
        }
      + group3: {
            deep: {
                id: {
                    number: 45
                }
            }
            fee: 100500
        }
    }
    """


    # for key, value in dict_1.items():
    #     if isinstance(value, str):
    #         if (key, value) in dict_2.items():
    #             diff_dict[f"{' = '}{key}"] = value
    #
    # for key, value in dict_1.items():
    #     if isinstance(value, str):
    #         if key not in dict_2.keys():
    #             diff_dict[f"{MINUS}{key}"] = value
    #
    # for key, value in dict_2.items():
    #     if isinstance(value, str):
    #         if (key, value) not in dict_1.items():
    #             diff_dict[f"{PLUS}{key}"] = value
    #
    # for key, value in dict_1.items():
    #     if isinstance(value, dict):
    #         if key not in dict_2.keys():
    #             diff_dict[f"{MINUS}{key}"] = value
    #
    # for key, value in dict_2.items():
    #     if isinstance(value, dict):
    #         if key not in dict_1.keys():
    #             diff_dict[f"{PLUS}{key}"] = value
    #
    # for key, value in dict_1.items():
    #     if isinstance(value, dict):
    #         if key in dict_2.keys():
    #             diff_dict[f"{' ~ '}{key}"] = create_diff_dict(value, value)

    return diff_dict


            # def create_diff_string(diff_list):
            #     # сортируем по алфавиту
            #     sorted_diff_list = sorted(diff_list, key=lambda x: x[4:])
            #
            #     # diff = '{'
            #     # for _ in sorted_diff_list:
            #     #     diff = f"{diff}\n{_}"
            #     #
            #     # return diff + '\n}'
            #     sorted_diff_dict = sorted_diff_list
            #     # return sorted_diff_list
            #     return sorted_diff_dict


def stringify(obj, level=0):
    spaces_count = 2
    space = " "

    if isinstance(obj, dict):
        result = "{\n"
        spaces = space * spaces_count * level

        for key, value in obj.items():
            string_value = stringify(value, level + 1)
            result += f"{spaces} {key}: {string_value}\n"

        result += f"{spaces}{'}'}"
    else:
        result = str(obj)

    return result


def generate_diff(path_1, path_2):
    dict_1 = file_parser(path_1)
    dict_2 = file_parser(path_2)

    diff_list = create_diff_dict(dict_1, dict_2)

    return stringify(diff_list)