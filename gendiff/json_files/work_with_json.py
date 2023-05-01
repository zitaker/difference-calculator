import json
import os


def generate_diff():

    # вводим два файла
    string_as_json_format1 = open('file1_json.json')
    obj1 = json.loads(string_as_json_format1.read())

    string_as_json_format2 = open('file2_json.json')
    obj2 = json.loads(string_as_json_format2.read())
#########################
    # PLUS = " + "
    # MINUS = " - "
    # SPASE = "   "
    #
    # obj11_list_result = list()
    # obj22_list_result = list()
    #
    # obj11_list = list(obj1.items())
    # obj22_list = list(obj2.items())
    #
    #
    # for key in obj11_list:
    #     obj22_list_result.append(f'{choosing_constants}{key}')
    # print(type(obj11_list), obj11_list_result)
    #
    # for key in obj22_list:
    #     obj22_list_result.append(f'{choosing_constants}{key}')
    # print(type(obj22_list), obj22_list_result)
########################
    # передаем в словарь файлы из первого файла
    result_duplicate_delete = dict()
    result_duplicate_delete.update(obj1)

    # удаляем из словаря файлы, которые есть в обоих файлах
    for key in obj1:
        if key in obj2 and obj1[key] == obj2[key]:
            result_duplicate_delete.pop(key)

    # переводим все в str и складываем словарь с вторым файлом
    obj1_str = str(result_duplicate_delete)
    obj2_str = str(obj2)
    obj_str = obj1_str + obj2_str

    # производим редактирование строки
    obj_str1 = obj_str.replace("}{", ", ")
    obj_str2 = obj_str1.replace("{", "")
    obj_str3 = obj_str2.replace("}", "")

    # переводим в list для вывода в алфавитном порядке
    list_obj = obj_str3.split(', ')
    list_obj.sort()

    # переводим обратно в str и редактируем строку
    obj_str4 = str(list_obj)
    obj_str5 = obj_str4.replace('[', '')
    obj_str6 = obj_str5.replace(']', '')
    obj_str7 = obj_str6.replace('"', '')
    obj_str4 = obj_str7.replace(', ', '\n')

    # отправляем в файл
    result_txt = open('result.txt', 'w')
    result_txt.write(obj_str4)





generate_diff()

result_reading = open('result.txt', 'r')
print(result_reading.read())

