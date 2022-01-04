from random import random
from math import pi
from time import time_ns

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
        self.breedTime = time_ns()
