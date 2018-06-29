#!/usr/bin/env python3

import datetime


def banner():
    print('-----------------------------------------')
    print('         The Birthday App                ')
    print('-----------------------------------------')


def get_birthday():
    birth_year = int(input('What year where you born [YYYY]? '))
    birth_day = int(input('What day where you born [DD]? '))
    birth_month = int(input('What month where you born [MM]? '))

    birthday = datetime.date(birth_year, birth_month, birth_day)

    return (birthday)

def get_day_until_birthday(user_birthday):
    today = datetime.date.today()
    target_date = datetime.date(today.year,user_birthday.month,user_birthday.day)
    difference = today - target_date
    return difference.days

def birthday_message(days_left):
    if days_left == 0:
        print('Happy Birthday')
    elif days_left < 0:
        print('Your Birthday is in {} days!'.format(-days_left))
    elif days_left > 0:
        print('Your Birthday was {} days ago!'.format(days_left))
    else:
        print('Error: Danger Wil Robinson, danger how did you get here')


banner()
user_birthday = get_birthday()
#print(user_birthday)
days_left = get_day_until_birthday(user_birthday)
#print(days_left)
birthday_message(days_left)


