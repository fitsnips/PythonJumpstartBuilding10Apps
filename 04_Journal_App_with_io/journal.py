#!/usr/bin/env python3


def open_journal(jname):
    print('Opening journal {}'.format(jname))


def add_entry():
    entry = input('What would you like to add? ')
    print('Adding entry to  journal {}'.format(entry))


def list_entries():
    entry_count = 1 #TODO get actual count
    print('You have {} journal entries: '.format(entry_count))

def close_journal():
    print('Closing journal {}'.format(jname))
