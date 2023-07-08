import json
import os
import sys


# method that takes json files and returns their lengths 
def files_length(file):
    print(len(file))
    menu()


# writes data into a give file
def write_file(data, file_name):
    application_path = get_os_file_path()
    with open(os.path.join(application_path, file_name), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    f.close()


# writes all the duplicate values to a file
def write_duplicates(data, file_name):
    application_path = get_os_file_path()
    with open(os.path.join(application_path, file_name), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    f.close()


# reads a json file and parses its data 
def read_file(file_name):
    file = open(file_name, 'r', encoding="utf8")
    file_data = file.read()
    file.close()
    return json.loads(file_data)


# gets the current location of the program in the os
def get_os_file_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    elif __file__:
        return os.path.dirname(__file__)


# checks a json file for duplicates and creates a new output file without them
def parse_duplicates(file_data, field):
    print('Starting duplicate removal tool...')
    result_items = []
    added_keys = []
    duplicates = []
    for i, item in enumerate(file_data):
        if len(result_items) == 0 or item[field] not in added_keys:
            result_items.append(item)
            added_keys.append(item[field])
        else:
            duplicates.append(item)
        print('Parsing ' + str(i + 1) + ' of ' + str(len(file_data)))

    write_file(result_items, 'parsed_output.json')
    write_duplicates(duplicates, 'duplicates.json')
    print('\nNumber of duplicates ', len(file_data) - len(result_items))
    userinput = input('\nCompleted! A new file has been created. Continue? (y/n)')
    if userinput == 'yes' or userinput == 'y':
        menu()


# the user menu with options for different funtions
def menu():
    print('Please choose an option:')
    print('1 - Compare files lengths')
    print('2 - Remove duplicates - Array of objects')
    option = input()

    if len(option) > 0:
        if option == '1':
            file_name = input('File name: ')
            parsed_data = read_file(file_name)
            files_length(parsed_data)
            menu()
        elif option == '2':
            file_name = input('File name: ')
            try:
                parsed_data = read_file(file_name)
                field_name = input('Field name to check duplicates for: ')
                parse_duplicates(parsed_data, field_name)
            except Exception as e:
                print('\nFile is invalid or not found. Error: {error} \n'.format(error=e))
                menu()
        else:
            print('Invalid option')
            menu()
    else:
        print('Something went wrong')
        menu()


menu()

# TODO deal with nested values
# def check_nested(file_data):
#     if isinstance(file_data, dict):
#         print('is dict')
#     elif isinstance(file_data, list):
#         print('list')
#
#     for key, value in file_data.items():
#         if isinstance(value, dict):
#             print('value dict')
#         elif isinstance(value, list):
#             for val in value:
#                 if isinstance(val, str):
#                     print('value str')
#                     pass
#                 elif isinstance(val, list):
#                     print('value list')
#                     pass
#                 elif isinstance(val, dict):
#                     print('value dict')
#                     pass
#                 else:
#                     parse_duplicates(file_data, 'field')
