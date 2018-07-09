#!/usr/bin/env python3
import random

from actors import Wizard, Creature


def main():
    banner()
    game_loop()


def banner():
    print('-------------------------------------')
    print('          Wizard Game App            ')
    print('-------------------------------------')


def game_loop():

    creatures = [
        Creature('Toad', 100),
        Creature('Tiger', 12),
        Creature('Bat', 3),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000)
    ]

    #print(creatures)

    hero = Wizard('Gandolf', 75)


    while True:

        active_creature = random.choice(creatures)

        print('A level {} {} has appeared from a dark and foggy forest ...'
              .format(active_creature.level, active_creature.name))


        cmd = input('Do you [a]ttack, [r]un away , or [l]ook around: ').rstrip().lower()
        if cmd == 'a':
            hero.attack(active_creature)
        elif cmd == 'r':
            print('run')
        elif cmd == 'l':
            print('look around')
        else:
            print('OK exiting game ... goodbye!')
            break





if __name__ == '__main__':
    main()
