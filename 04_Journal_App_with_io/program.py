#!/usr/bin/env python3

import journal
import sys

def banner():
    print('----------------------------------------------')
    print('                Daily Journal                 ')
    print('----------------------------------------------')


def menu():
    menu_selection = input('What would you like to do with your journal? [L]ist, [A]dd, E[x]it ').upper().strip()
    return menu_selection


def new_entry(j_entries):
    entry = input('What would you like to add? ')
    journal_entries = journal.add_entry(j_entries, entry)
    print('Added entry to journal {}'.format(entry))
    return journal_entries


def quit(name, entries):
    print()
    journal.save(name, entries)
    print('Goodbye')
    sys.exit()


def main():
    journal_name = 'default'
    menu_choice = 'EMPTY'
    banner()

    journal_entries = journal.load(journal_name)


    while menu_choice != 'X' and menu_choice:
        menu_choice = menu()

        if menu_choice == 'L':
            journal.list_entries(journal_entries)
        elif menu_choice == 'A':
            journal_entries = new_entry(journal_entries)
        elif menu_choice != 'X' and menu_choice:
            print('Error: the sky is rising AND your entry is not understood')

    quit(journal_name, journal_entries)



if __name__ == '__main__':
    main()