#!/usr/bin/env python3
import glob
import os
import collections

SearchResult = collections.namedtuple('SearchResult',
                                      'filename, fileline_number, found_string' )

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
    found_strings = search_dir(user_string,search_path)
    print_found_files(found_strings)
    print_summary(found_strings)

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
    return user_string.lower()

def search_dir(user_string, search_path):
    found_strings = []

    items = glob.glob(os.path.join(search_path, '*'))

    print('Searching {} for {}'.format(search_path, user_string))

    for item in items:
        full_item_path = os.path.join(search_path, item)
        if os.path.isdir(full_item_path):
            matches = search_dir(user_string, full_item_path)
            found_strings.extend((matches))
        else:
            matches = search_file(full_item_path, user_string)
            found_strings.extend(matches)

    return found_strings

def search_file(path, text):
    matches = []
    with open(path, 'r', encoding='utf-8') as fin:

        for count, line in enumerate(fin):
            if line.lower().find(text) >= 0:
                m = SearchResult(filename=path,fileline_number=count+1, found_string=line )
                matches.append(m)
        return matches

def print_found_files(found_strings):

    if found_strings:
        for found_string in found_strings:
            print('-------------- MATCH -------------')
            print('file: ' + found_string.filename)
            print('line: {}'.format(found_string.fileline_number))
            print('match: ' + found_string.found_string.strip())
            print()


def print_summary(found_strings):
    print('{} total matches.'.format(len(found_strings)))
    print('End of search')


if __name__ == '__main__':
    main()