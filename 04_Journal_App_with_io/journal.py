#!/usr/bin/env python3

import os

def load(jname):
    """
    This method creates a journal
    :param jname: The journal file name
    :return jentries: Array of lines of the journal file
    """
    filename = get_full_pathname(jname)
    jentries = []

    if os.path.exists(filename):
        print('Reading in journal .... {}'.format(filename))
        print()
        with open(filename) as fin:
            for entry in fin.readlines():
                jentries.append(entry.rstrip())
    return jentries

def save(jname, journal_data):
    filename = get_full_pathname(jname)
    print('.... saving your journal to {}'.format(filename))

    if journal_data:
        with open(filename, 'w') as fout:
            for entry in journal_data:
                fout.write(entry + '\n')


def get_full_pathname(jname):
    filename = os.path.abspath(os.path.join('.', 'journals', jname + '.jrl'))
    return filename


def add_entry(jdata, entry):
    jdata.append(entry)
    return jdata

def list_entries(journal_entries):
    print('Your journal entries: ')
    entries = reversed(journal_entries)
    for key,entry in enumerate(entries):
        print('* [{}] {}'.format(key + 1,entry))


