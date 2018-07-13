#!/usr/bin/env python3


def main():
    banner()
    search_path = get_search_path()
    user_string = get_user_string()
    found_count, found_strings = search_for_string(user_string,search_path)
    print_found_files(found_strings)
    print_summary(found_count)

def banner():
    print('--------------------------------------------')
    print('               FILE SEARCH                  ')
    print('--------------------------------------------')


def get_search_path():
    search_path = input('What directory do you want to search: ')
    return search_path


def get_user_string():
    user_string = input('What string are you looking for: ')
    return user_string

def search_for_string(user_string, search_path):

    found_count = 0

    print('Searching {} for {}'.format(search_path, user_string))
    found_strings = []

    #TODO preform actual search
    return found_count, found_strings


def print_found_files(found_strings):

    if found_strings:
        for filname, fileline_number, found_string in found_strings:
            filename = 'file_name_place_holder'
            fileline_number = 'fileline_number_place_holder'
            found_string = 'found_sting_place_holder'
            print('{}, {}>> {}'.format(filename, fileline_number, found_string))


def print_summary(number_found):
    print('{} total matches.'.format(number_found))
    print('End of search')


if __name__ == '__main__':
    main()