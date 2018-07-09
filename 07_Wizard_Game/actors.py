#!/usr/bin/env python3
import random


class Wizard:
    def __init__(self, the_name, the_level):
        self.name = the_name
        self.level = the_level

    def attack(self, creature):
        print("The wizard {} attacks {}!". format(
            self.name, creature.name
        ))

        my_roll = random.randint(1, 12) * self.level
        creature_role = random.randint(1, 12) * creature.level

        print('You rolled {} ... '.format(my_roll))
        print('{} rolls {} ... '.format(creature.name, creature_role))


        if my_roll >= creature_role:
            print('The wizrad has handily triumped over {}'.format(creature.name))
            return True
        else:
            print('The wizard has been DEFEATED!!!')
            return False

class Creature:
    def __init__(self, the_name, the_level):
        self.name = the_name
        self.level = the_level

    def __repr__(self):
        return "Creature of {} of level {}".format(
            self.name, self.level
        )