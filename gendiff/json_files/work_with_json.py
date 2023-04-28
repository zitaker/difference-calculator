import json
import os





# str_json1 = '''
# {
#   "host": "hexlet.io",
#   "timeout": 50,
#   "proxy": "123.234.53.22",
#   "follow": false
# }
# '''
#
# str_json2 = '''
# {
#   "host": "hexlet.io",
#   "timeout": 50,
#   "proxy": "123.234.53.22",
#   "follow": false
# }
# '''
# print(type(str_json1))
#
# files = json.loads(str_json1)
# print(type(files))
# print(files)

def generate_diff():
    way1 = open('file1_json.json', 'r')
    way2 = open('file2_json.json', 'r')
    print(way1.read(), way2.read())

    with open('file1_json.json') as file1:
        # print(type(file1.read()))
        for line in file1:
            filelist1 = line.split()
            with open('file2_json.json') as file2:
                for line in file2:
                    filelist2 = line.split()
                    result = list(set(filelist1) & set(filelist2))
                    if result == []:
                        continue
                    else:
                        print(result, end='\n')


generate_diff()