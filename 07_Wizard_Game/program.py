#!/usr/bin/env python3



def main():
    banner()
    game_loop()


def banner():
    print('-------------------------------------')
    print('          Wizard Game App            ')
    print('-------------------------------------')


def game_loop():
    while True:
        cmd = input('Do you [a]ttack, [r]un away , or [l]ook around: ').rstrip().lower()
        if cmd == 'a':
            print('attack')
        elif cmd == 'r':
            print('run')
        elif cmd == 'l':
            print('look around')
        else:
            print('OK exiting game ... goodbye!')
            break





if __name__ == '__main__':
    main()
