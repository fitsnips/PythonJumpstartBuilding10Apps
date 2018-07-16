#!/usr/bin/env python3
import os
import collections


def main():
    banner()
    datafile = get_data_file()
    data = load_data(datafile)




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
    with open(datafile, 'r', encoding='utf-8') as fin:
        header = fin.readline().strip()
        for line in fin:
           line_data = line.strip().split(',')
           lines.append(line_data)

    print('... done')
    print('Header: ' + header)
    for line in lines[:5]:
        print(line)
    print()

    return lines



if __name__ == '__main__':
    main()