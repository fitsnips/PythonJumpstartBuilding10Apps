#!/usr/bin/env python3
import random
import time

from actors import Wizard, Creature, SmallAnimal, Dragon



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
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, scaliness=20,breaths_fire=True),
        Dragon('Blue Dragon', 50, scaliness=100, breaths_fire=False),
        Wizard('Evil Wizard', 1000)
    ]

    hero = Wizard(player_name, 75)


    while True:

        active_creature = random.choice(creatures)

        print()
        print('A level {} {} has appeared from a dark and foggy forest ...'
              .format(active_creature.level, active_creature.name))



        cmd = input('[Level {}] Do you [a]ttack, [r]un away , [t]rain, [l]ook around, or E[x]it game: '.format(hero.level)).rstrip().lower()
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
        elif cmd == 'x':
            print('OK exiting game ... goodbye!')
            break
        else:
            print('Try again, unknown command!')

        if not creatures:
            print()
            print('*************************************************')
            print('You have defeated all your enemies, well done {}'.format(hero.name))
            break




if __name__ == '__main__':
    main()
