import json
import os
import sys
import time


# method that takes json files and returns their lengths
def files_length(file):
    print('\nFile length: {length}'.format(length=len(file)))


# writes data into a give file
def write_file(data, file_name):
    application_path = get_os_file_path()
    with open(os.path.join(application_path, file_name), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    f.close()


# reads a json file and parss its data
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


# Simple continue or not user prompt
def continue_prompt():
    user_input = input('\nContinue? yes/no (y/n) ')
    if user_input == 'yes' or user_input == 'y':
        menu()


# Checks if the file exists and is valid
def validate_file(file_name):
    try:
        return read_file(file_name)
    except Exception as e:
        print(
            '\nFile is invalid or not found. Error: {error} \n'.format(error=e))
        menu()


# Removes search field names spaces and commas
def format_search_fields(field_names):
    if ',' in field_names:
        field_names = field_names.replace(' ', '')
        field_names = field_names.split(',')
    elif ' ' in field_names:
        field_names = field_names.split(' ')

    return field_names


# checks a json file for duplicates and creates a new output file without them
def parse_duplicates(file_data, fields):
    print('Starting empty removal tool...')
    start_time = time.time()
    result_items = []
    duplicates = []
    checked_objects = []

    def is_duplicate(json_data, target_field):
        if isinstance(json_data, dict):
            for key, value in json_data.items():
                if key == target_field:
                    item_object = {key: value}
                    if len(result_items) == 0 or (
                            item_object not in checked_objects and value):
                        if item not in result_items:
                            result_items.append(item)
                        checked_objects.append(item_object)
                    # TODO when a UI is made, include option to include empty/null values
                    elif value and item not in duplicates:
                        duplicates.append(item)
                elif isinstance(value, (dict, list)):
                    is_duplicate(value, target_field)
            if json_data not in duplicates and json_data not in result_items:
                result_items.append(json_data)
        elif isinstance(json_data, list):
            for list_item in json_data:
                is_duplicate(list_item, target_field)

    for i, item in enumerate(file_data):
        if isinstance(fields, str):
            is_duplicate(item, fields)
        else:
            for field in fields:
                is_duplicate(item, field)
        print(f'Parsing: {int((i / len(file_data)) * 100)}%')

    write_file(result_items, 'no_duplicates.json')
    write_file(duplicates, 'duplicates.json')
    print('\nNumber of duplicates ', len(duplicates))
    print("\nParse completed! Parsed and duplicates files have been created. It took %s seconds" %
          round((time.time() - start_time), 2))


# Removes empty objects from the file based on empty fields
def parse_empty_fields(file_data, fields):
    print('Starting empty removal tool...')
    start_time = time.time()
    result_items = []
    empty_items = []

    def is_empty(json_data, target_field):
        if isinstance(json_data, dict):
            for key, value in json_data.items():
                if key == target_field:
                    if not value:
                        if item not in empty_items:
                            empty_items.append(item)
                    else:
                        if item not in result_items:
                            result_items.append(item)
                elif isinstance(value, (dict, list)):
                    is_empty(value, target_field)
            if item not in empty_items and item not in result_items:
                result_items.append(item)
        elif isinstance(json_data, list):
            for list_item in json_data:
                is_empty(list_item, target_field)

    for i, item in enumerate(file_data):
        if isinstance(fields, str):
            is_empty(item, fields)
        else:
            for field in fields:
                is_empty(item, field)
        print(f'Parsing: {int((i / len(file_data)) * 100)}%')

    write_file(result_items, 'no_empties.json')
    write_file(empty_items, 'empties.json')
    print('\nNumber of empty items ', len(empty_items))
    print("\nParse completed! Parsed and empties files have been created. It took %s seconds" %
          round((time.time() - start_time), 2))


# The user menu with options for different functions
def menu():
    print('Please choose an option:')
    print('1 - File length')
    print('2 - Remove duplicates - Array of objects [{}]')
    print('3 - Remove from file based on empty fields')

    option = input()
    if len(option) > 0:
        if option == '1':
            file_name = input('File name: ')
            parsed_data = validate_file(file_name)
            files_length(parsed_data)
            continue_prompt()
        elif option == '2':
            file_name = input('File name: ')
            parsed_data = validate_file(file_name)
            field_names = input(
                'Fields to check duplicates for (comma or space separated): ')
            field_names = format_search_fields(field_names)
            parse_duplicates(parsed_data, field_names)
            continue_prompt()
        elif option == '3':
            file_name = input('File name: ')
            parsed_data = validate_file(file_name)
            field_names = input(
                'Fields to check empty for (comma or space separated): ')
            field_names = format_search_fields(field_names)
            parse_empty_fields(parsed_data, field_names)
            continue_prompt()
    else:
        print('Something went wrong')
        menu()


menu()
