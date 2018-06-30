#!/usr/bin/env python3


def open_journal(jname):
    print('Opening journal {}'.format(jname))


def add_entry(journal_entries):
    entry = input('What would you like to add? ')
    journal_entries.append(entry)
    print('Adding entry to  journal {}'.format(entry))
    #list_entries(journal_entries)


def list_entries(journal_entries):
    print('Your journal entries: ')
    entries = reversed(journal_entries)
    for key,entry in enumerate(entries):
        print('* [{}] {}'.format(key + 1,entry))

def close_journal():
    print('Closing journal {}'.format(jname))
