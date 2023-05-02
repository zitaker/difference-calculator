import json
import os


def generate_diff():

    # вводим два файла
    string_as_json_format1 = open('file1_json.json')
    obj1 = json.loads(string_as_json_format1.read())

    string_as_json_format2 = open('file2_json.json')
    obj2 = json.loads(string_as_json_format2.read())
########################
    PLUS = " + "
    MINUS = " - "
    SPASE = "   "

    result_obj1_in_list = list()
    result_obj2_in_list = list()

    obj1_translate_in_list = list(obj1.items())
    obj2_translate_in_list = list(obj2.items())

    result_obj1_in_list.append(obj1_translate_in_list)
    result_obj2_in_list.append(obj2_translate_in_list)

    unified_obj_list = result_obj1_in_list + result_obj2_in_list
    ##############################################
    # первый list
    result_obj1_in_str = str(result_obj1_in_list)
    result_obj1_in_str1 = result_obj1_in_str.split('),')
    result_obj1_in_str1.sort()
    result_obj1_in_str2 = str(result_obj1_in_str1)
    result_obj1_in_str3 = result_obj1_in_str2.replace('[', '')
    result_obj1_in_str4 = result_obj1_in_str3.replace(']', '')
    result_obj1_in_str5 = result_obj1_in_str4.replace("',", ':')
    result_obj1_in_str6 = result_obj1_in_str5.replace("(", '')
    result_obj1_in_str7 = result_obj1_in_str6.replace(")", '')
    result_obj1_in_str8 = result_obj1_in_str7.replace('" ', '')
    result_obj1_in_str9 = result_obj1_in_str8.replace('"', '')
    result_obj1_in_str10 = result_obj1_in_str9.replace("'", '')

    result_obj1_in_str11 = result_obj1_in_str10.split(', ')
    result_obj1_in_str11.sort()
    # print(result_obj1_in_str11)

    # второй list
    result_obj2_in_str = str(result_obj2_in_list)
    result_obj2_in_str1 = result_obj2_in_str.split('),')
    result_obj2_in_str1.sort()
    result_obj2_in_str2 = str(result_obj2_in_str1)
    result_obj2_in_str3 = result_obj2_in_str2.replace('[', '')
    result_obj2_in_str4 = result_obj2_in_str3.replace(']', '')
    result_obj2_in_str5 = result_obj2_in_str4.replace("',", ':')
    result_obj2_in_str6 = result_obj2_in_str5.replace("(", '')
    result_obj2_in_str7 = result_obj2_in_str6.replace(")", '')
    result_obj2_in_str8 = result_obj2_in_str7.replace('" ', '')
    result_obj2_in_str9 = result_obj2_in_str8.replace('"', '')
    result_obj2_in_str10 = result_obj2_in_str9.replace("'", '')

    result_obj2_in_str11 = result_obj2_in_str10.split(', ')
    result_obj2_in_str11.sort()
    # print(result_obj2_in_str11)

    # print(obj1_translate_in_list)
# unified_obj_str = str(unified_obj_list)
# unified_obj15 = unified_obj_str.split('),')
# unified_obj15.sort()
# print(unified_obj15)
# result_obj1_in_list_mathematical_symbol = list()
# print(result_obj1_in_list_mathematical_symbol)
################################################

    unified_obj_str = str(unified_obj_list)

    unified_obj1 = unified_obj_str.replace('[', '')
    unified_obj2 = unified_obj1.replace(']', '')
    unified_obj3 = unified_obj2.replace("',", ':')
    unified_obj4 = unified_obj3.replace("(", '')
    unified_obj5 = unified_obj4.replace(")", '')

    unified_obj6 = unified_obj5.split(', ')
    unified_obj6.sort()
    unified_obj7 = str(unified_obj6)

    unified_obj8 = unified_obj7.replace('[', '')
    unified_obj9 = unified_obj8.replace(']', '')
    unified_obj10 = unified_obj9.replace('"', '')
    unified_obj11 = unified_obj10.replace("'", '')

    unified_obj12 = unified_obj11.split(', ')
    unified_obj12.sort()
    # print(unified_obj12)


    result = list()
    for key in unified_obj12:
        if key in result_obj1_in_str11 and key not in result_obj2_in_str11:
            result.append(f"{MINUS}{key}")

    for key in unified_obj12:
        if key in result_obj2_in_str11 and key not in result_obj1_in_str11:
            result.append(f"{PLUS}{key}")

    for key in unified_obj12:
        if key in result_obj2_in_str11 and key in result_obj1_in_str11:
            result.append(f"{SPASE}{key}")

    result_str = str(result)
    result_str1 = result_str.replace('[', '')
    result_str2 = result_str1.replace(']', '')
    result_str3 = result_str2.replace("' ", '')
    result_str4 = result_str3.replace("'", '')

    result_str5 = result_str4.split(', ')
    ####### тут
    res = sorted(result_str5, key=lambda x: x[2:])
    ####### тут
    # result_str5.sort()
    print(res)

    # for _ in result_str5:
    #     print(_[2:])
    # print('@@@@@@@@@@@@@@@@@@')
    # for _ in unified_obj12:
    #     print(_)
    # d = list('_[2:]')
    # for _ in unified_obj12:
    #     if _[2:] in result_str5 and unified_obj12[_] == result_str5[d]:
    #         unified_obj13 = unified_obj12.replace(_, result_str5[_])
    # print(unified_obj13)


    # for key in obj1_translate_in_list:
    #     if key not in obj2_translate_in_list:
    #         result_obj1_in_list.append(f'{MINUS}{key}')
    #
    # for key in obj2_translate_in_list:
    #     if key not in obj1_translate_in_list:
    #         result_obj2_in_list.append(f'{PLUS}{key}')
    #
    # for key in obj1_translate_in_list:
    #     if key in obj2_translate_in_list:
    #         result_obj2_in_list.append(f'{SPASE}{key}')
    # unified_obj = result_obj1_in_list + result_obj2_in_list
    # unified_obj.sort()



#######################
    # # передаем в словарь файлы из первого файла
    # result_duplicate_delete = dict()
    # result_duplicate_delete.update(obj1)
    #
    # # удаляем из словаря файлы, которые есть в обоих файлах
    # for key in obj1:
    #     if key in obj2 and obj1[key] == obj2[key]:
    #         result_duplicate_delete.pop(key)
    #         # obj22_list_result.append(f'{SPASE}{key}')
    #
    # # переводим все в str и складываем словарь с вторым файлом
    # obj1_str = str(result_duplicate_delete)
    # obj2_str = str(obj2)
    # obj_str = obj1_str + obj2_str
    #
    # # производим редактирование строки
    # obj_str1 = obj_str.replace("}{", ", ")
    # obj_str2 = obj_str1.replace("{", "")
    # obj_str3 = obj_str2.replace("}", "")
    #
    # # переводим в list для вывода в алфавитном порядке
    # list_obj = obj_str3.split(', ')
    # list_obj.sort()
    #
    # # переводим обратно в str и редактируем строку
    # obj_str4 = str(list_obj)
    # obj_str5 = obj_str4.replace('[', '')
    # obj_str6 = obj_str5.replace(']', '')
    # obj_str7 = obj_str6.replace('"', '')
    # obj_str4 = obj_str7.replace(', ', '\n')
    #
    # # отправляем в файл
    # result_txt = open('result.txt', 'w')
    # result_txt.write(obj_str4)





generate_diff()

# result_reading = open('result.txt', 'r')
# print(result_reading.read())

