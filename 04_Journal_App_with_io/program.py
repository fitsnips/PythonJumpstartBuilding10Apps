#!/usr/bin/env python3

import journal
import sys

def banner():
    print('----------------------------------------------')
    print('                Daily Journal                 ')
    print('----------------------------------------------')

def menu():
    menu_selection = input('What would you like to do? [L]ist, [A]dd, E[x]it').upper()
    return menu_selection





def main():
    journal_name = 'default.journal'
    loop = True
    banner()

    # Read in our journal
    journal.open_journal(journal_name)

    while loop != 'e':
        menu_choice = menu()

        if menu_choice == 'L':
            journal.list_entries()
        elif menu_choice == 'A':
            journal.add_entry()
        elif menu_choice == 'X':
            sys.exit()
        else:
            print('Error: the sky is rising and your entry is not understood')



main()