#!/usr/bin/env python3
import os
import collections


def main():
    banner()
    datafile = get_data_file()
    data = load_data(datafile)
    header = data[0]
    print(header)
    print()

    for id,line in enumerate(data):
        if id != 0:
            print(line)


def banner():
    print('----------------------------------------------')
    print('              Real Estate App                 ')
    print('----------------------------------------------')
    print()

def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'home_data.csv')

def load_data(datafile):

    lines = []

    print('Loading CSV real estate data from ... {}'.format(datafile), end=' ')
    with open(datafile, 'r') as fin:
       for line in fin:
           lines.append(line)
    print('... done')
    print()

    return lines



if __name__ == '__main__':
    main()