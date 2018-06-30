#!/usr/bin/env python3

import journal
import sys

def banner():
    print('----------------------------------------------')
    print('                Daily Journal                 ')
    print('----------------------------------------------')

def menu():
    menu_selection = input('What would you like to do with your journal? [L]ist, [A]dd, E[x]it').upper().strip()
    return menu_selection





def main():
    journal_name = 'default.journal'
    journal_entries = []
    menu_choice = True
    banner()

    # Read in our journal
    journal.open_journal(journal_name)

    while menu_choice != 'x':
        menu_choice = menu()

        if menu_choice == 'L':
            journal_entries = journal.list_entries(journal_entries)
        elif menu_choice == 'A':
            journal.add_entry(journal_entries)
        elif menu_choice == 'X':
            print()
            print('Goodbye')
            sys.exit()
        else:
            print('Error: the sky is rising AND your entry is not understood')



main()