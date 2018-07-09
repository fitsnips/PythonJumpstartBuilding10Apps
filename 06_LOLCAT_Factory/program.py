#!/usr/bin/env python3
import os
import platform
import subprocess
import cats_service

def main():
    banner()
    # get or create output folder
    folder = get_or_create_output_folder()
    print('Found or created: ' + folder)
    # download cat files
    download_cats(folder)
    # display cats
    show_cats(folder)


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
    print('Contacting server to download cats ... ')
    cat_count = 8
    for i in range(1,cat_count+1):
        name = 'lolcat_{}'.format(i)
        print('Downloading cat {}'.format(name))
        cats_service.get_cat(target_folder, name)
    print('Downloading completed.')

def show_cats(folder):
    # open the folder in OS file
    OS = platform.system()
    print('Displaying cats in OS window: ')
    if OS == 'Darwin':
        subprocess.call(['open', folder])
    elif OS == 'Windows':
        subprocess.call(['explorer', folder])
    elif OS == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print('Sorry we do not support automated window browsing on the {} operating system'.format(OS))

if __name__ == '__main__':
    main()
