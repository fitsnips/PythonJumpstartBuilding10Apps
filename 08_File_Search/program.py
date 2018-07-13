#!/usr/bin/env python3
import os

def main():
    banner()
    search_path = get_search_path()
    if not search_path:
        print('Sorry we can not search that location.')
        return
    user_string = get_user_string()
    if not user_string:
        print('Sorry we can not search for that file.')
        return
    found_count, found_strings = search_for_string(user_string,search_path)
    print_found_files(found_strings)
    print_summary(found_count)

def banner():
    print('--------------------------------------------')
    print('               FILE SEARCH                  ')
    print('--------------------------------------------')


def get_search_path():
    search_path = input('What directory do you want to search: ')
    if not search_path or not search_path.strip():
        return None

    if not os.path.isdir(search_path):
        return None

    return os.path.abspath(search_path)


def get_user_string():
    user_string = input('What string are you looking for [ single phrase only]: ')
    if not user_string or not user_string.strip():
        return None
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