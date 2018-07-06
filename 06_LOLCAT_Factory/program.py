#!/usr/bin/env python3
import os
import cats_service

def main():
    banner()
    # get or create output folder
    folder = get_or_create_output_folder()
    print('Found or created: ' + folder)
    # download cat files
    download_cats(folder)
    # display cats


def banner():
    print('-----------------------------------')
    print('          Cat Factory App          ')
    print('-----------------------------------')


def get_or_create_output_folder():
    # print(__file__)
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at: '.format(full_path))
        os.mkdir(full_path)

    return full_path

def download_cats(target_folder):
    cat_count = 8
    for i in range(1,cat_count+1):
        name = 'lolcat_{}'.format(i)
        cats_service.get_cat(target_folder, name)


if __name__ == '__main__':
    main()
