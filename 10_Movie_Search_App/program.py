#!/usr/bin/env python3
import urllib3


def main():
    banner()
    search_title = get_movie_title()
    found_titles = find_movie_by_title(search_title)
    print_found_titles(found_titles)


def banner():
    print('------------------------------------------------------')
    print('                 Movie Search App                     ')
    print('------------------------------------------------------')
    print()

def get_movie_title():
    title = input=('What movie title would you like to search for: ')
    return title

def find_movie_by_title(search_string):
    url = movie_service.talkpython.fm/search_string

    try
    titles = { 'name': title, 'year': year }
    return titles

def print_found_titles(titles):
    for year, title in titles:
        print('{} - {}'.format(year, title))

if __name__ == '__main__':
    main()
