#!/usr/bin/env python3
import random
import time

class Creature:
    def __init__(self, the_name, the_level):
        self.name = the_name
        self.level = the_level  + (random.randint(0,10) * 10)

    def __repr__(self):
        return "Creature of {} of level {}".format(
            self.name, self.level
        )

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):

    def train(self):
        training_value = random.randint(0,25)

        if training_value == 0:
            print('Silence around you would be peaceful, at least more so then the birds '
                  'laughing at you. Gain {} levels. '.format(training_value))
            print()
        else:
            print('Training ... [ 5 seconds ]')
            time.sleep(5)
            self.level = self.level + training_value
            print('{} you have gained {} levels while training'.format(
                self.name, training_value
            ))
            print()

    def attack(self, creature):
        print("The wizard {} attacks {}!". format(
            self.name, creature.name
        ))

        my_roll = random.randint(1, 12) * self.level
        creature_role = creature.get_defensive_roll()

        print('You rolled {} ... '.format(my_roll))
        print('{} rolls {} ... '.format(creature.name, creature_role))
        print()


        if my_roll >= creature_role:
            print('The wizard has handily triumped over {}'.format(creature.name))
            self.level = (self.level + (creature.level // random.randint(1,10)))
            return True
        else:
            print('The wizard {} has been DEFEATED!!!'.format(self.name))
            # even in defeat we gain a little XP,  removed after adding training
            # self.level = (self.level + random.randint(1,50))
            return False

class SmallAnimal(Creature):
    def get_defensive_roll(self):
        modified_roll = super().get_defensive_roll() / 2
        return modified_roll

class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name,level)
        self.breaths_fire = breaths_fire
        self.scaliness = scaliness

        if breaths_fire:
            self.name = '[Fire Breathing] ' + self.name

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        # fire_modifier = None
        # if self.breaths_fire:
        #     fire_modifier = 5
        # else:
        #     fire_modifier = 1

        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scaliness / 10
        modified_roll = base_roll * fire_modifier
        return modified_roll










