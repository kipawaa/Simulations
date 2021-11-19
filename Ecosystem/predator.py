from creature import Creature
from math import dist, pi, sin, cos, atan2
from random import random

class Predator(Creature):
    def draw(self, canvas):
        canvas.create_polygon([self.x - 5, self.y - 5, self.x + 5, self.y - 5, self.x, self.y + 5], fill="red")

    def update(self, win_width, win_height, preyList):
        closest_prey = min([(dist((self.x, self.y), (prey.x, prey.y)), prey) for prey in preyList], key=lambda x:x[0])
        if closest_prey[0] < self.sightRange:
            direction = atan2(self.y - closest_prey[1].y, self.x - closest_prey[1].x)
            self.x += cos(self.direction) if 0 <= self.x + cos(self.direction) <= win_width else 0
            self.y += sin(self.direction) if 0 <= self.y + sin(self.direction) <= win_height else 0
        else:
            # change the direction by up to pi/6
            #self.direction += (2 * random() - 1) * pi / 12
            pass
        

        
