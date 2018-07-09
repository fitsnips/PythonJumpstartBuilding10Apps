#!/usr/bin/env python3
import random
import time

from actors import Wizard, Creature


def main():
    banner()
    player_name = get_player_name()
    game_loop(player_name)


def banner():
    print('-------------------------------------')
    print('          Wizard Game App            ')
    print('-------------------------------------')

def get_player_name():
    player_name = input('What shall we call you? ').rstrip()
    return player_name

def game_loop(player_name):

    creatures = [
        Creature('Toad', 100),
        Creature('Tiger', 12),
        Creature('Bat', 3),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000)
    ]

    hero = Wizard(player_name, 75)


    while True:

        active_creature = random.choice(creatures)

        print('A level {} {} has appeared from a dark and foggy forest ...'
              .format(active_creature.level, active_creature.name))



        cmd = input('[Level {}] Do you [a]ttack, [r]un away , [t]rain, or [l]ook around: '.format(hero.level)).rstrip().lower()
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('The wizard runs and hides taking time to recover ...')
                time.sleep(5)
                print('The wizard returns well rested.')
        elif cmd == 'r':
            print('The wizard {} has become unsure of his powers and flees'.format(hero.name))
        elif cmd == 'l':
            print('The wizard {} takes in the surroundings and sees:'.format(hero.name))
            for c in creatures:
                print(' * A {} of level {}'.format(c.name, c.level))
        elif cmd == 't':
            print('The wizard {} takes two sticks and waves them saying random phrases:'.format(hero.name))
            hero.train()
        else:
            print('OK exiting game ... goodbye!')
            break

        if not creatures:
            print('You have defeated all your enemies, well done {}'.format(hero.name))
            break




if __name__ == '__main__':
    main()
