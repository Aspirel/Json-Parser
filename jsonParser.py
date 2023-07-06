import json


# method that takes json files and returns their lengths 
def files_length(files):
    menu()


# writes data into a give file
def write_file(data, fileName):
    with open(fileName, 'w') as f:
        json.dump(data, f, indent=4)
        

# reads a json file and parses its data 
def read_file(file_name):
    file = open(file_name, 'r')
    file_data = file.read()
    return json.loads(file_data)


# checks a json file for duplicates and creates a new output file without them
def parse_duplicates(fileData, field, outputFileName):
    print('Starting duplicate removal tool...')
    result_items = []
    added_keys = []
    for i, item1 in enumerate(fileData):
        for item2 in fileData:
            if len(result_items) == 0 or item1[field] != item2[field] and item2[field] not in added_keys:
                result_items.append(item2)
                added_keys.append(item2[field])
        print('Parsing ' + str(i+1) + ' of ' + str(len(fileData)) + ' ')
    write_file(result_items, outputFileName)
    print('\nCompleted! A new file has been created. Continue? yes/no')
    if input() == 'yes':
        menu()
    

# the user menu with options for different funtions
def menu():
    print('Please choose an option:')
    print('1 - Compare files lengths')
    print('2 - Remove duplicates')
    option = input()
    
    if len(option) > 0:
        if option == '1':
            print('test')
            menu()
        elif option == '2':
            file_name = input('File name: ')
            try:
                parsed_data = read_file(file_name)
                field_name = input('Field name to check duplicates for: \n')
                output_file_name = input('Output file name: \n')
                parse_duplicates(parsed_data, field_name, output_file_name + '.json')
            except Exception as e: 
                print('\nFile is invalid or not found. Error: {error} \n'.format(error=e))
                menu()
        else:
            print('Invalid option')
            menu()
    else:
        print('Something went wrong')
        menu()


# TODO
# Need to check for supported file extensions. Need to store it and use it for the output file extension.
# Need to check for a file extension when after its input, if exists and is valid, keep it, otherwise,
# inform the user of the default extension .json and add it to the output file
menu()
