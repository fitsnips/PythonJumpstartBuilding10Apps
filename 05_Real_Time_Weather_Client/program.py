#!/usr/bin/env python3


def main():
    user_zip = False
    banner()
    user_zip = get_zipcode()
    print(user_zip)
    #TODO Get webpage
    #TODO Parse web data
    #TODO return weather


def banner():
    print('----------------------------------------')
    print('        WEATHER CLINT APP               ')
    print('----------------------------------------')
    print()


def get_zipcode():
    zipcode = input('What is your zipcode (e.g. 78660): ')
    return zipcode


if __name__ == '__main__':
    main()