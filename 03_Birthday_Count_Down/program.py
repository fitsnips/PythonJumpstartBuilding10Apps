#!/usr/bin/env python3

import datetime


def print_banner():
    print('-----------------------------------------')
    print('         The Birthday App                ')
    print('-----------------------------------------')


def get_birthday():
    birth_year = input('What year where you born [YYYY]? ')
    birth_day = input('What day where you born [DD]? ')
    birth_month = input('What month where you born [MM]? ')

    return (birth_year, birth_day, birth_month)

def get_day_until_birthday(b_year,b_day,b_month):
    today = datetime.datetime().now()
    print(today)



print_banner()
b_year,b_day,b_month = get_birthday()
days_left = get_day_until_birthday(b_year,b_day,b_month)


