from random import random
from math import pi

class Creature:
    def __init__(self, x, y, hunger, thirst, health, speed, sightRange):
        self.hunger = hunger
        self.thirst = thirst
        self.health = health
        self.x = x
        self.y = y
        self.speed = speed
        self.sightRange = sightRange
        self.direction = random() * 2 * pi

    def eat(self, amount=100):
        # maybe allow overeating and reduce speed??
        self.hunger = max(self.hunger + amount, 100)

    def drink(self, amount=100):
        self.thirst = max(self.thirst + amount, 100)

    def update(self):
        self.thirst -= 2
        self.hunger -= 1

        if (self.hunger > 30 and self.health < 100):
            self.health += 1
            self.hunger -= 1

        self.priority = "hunger" if self.hunger < self.thirst else "thirst"
