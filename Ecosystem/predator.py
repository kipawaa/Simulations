from creature import Creature
from math import dist, pi, sin, cos, atan2
from random import random

class Predator(Creature):
    def draw(self, canvas):
        canvas.create_polygon([self.x - 5, self.y - 5, self.x + 5, self.y - 5, self.x, self.y + 5], fill="red")

    def update(self, win_width, win_height, creatures, canvas):
        prey = min([(dist((self.x, self.y), (prey.x, prey.y)), prey) for prey in creatures[1]], key=lambda x:x[0])
        if prey[0] < self.sightRange:
            if prey[0] < 2.5:
                creatures[1].remove(prey[1])
            else:
                canvas.create_line(self.x, self.y, prey[1].x, prey[1].y)
                self.direction = atan2(prey[1].y - self.y, prey[1].x - self.x)
        else:
            # change the direction by up to pi/12
            self.direction += (2 * random() - 1) * pi / 12
            
        self.x += cos(self.direction) * self.speed if 0 <= self.x + cos(self.direction) * self.speed <= win_width else 0
        self.y += sin(self.direction) * self.speed if 0 <= self.y + sin(self.direction) * self.speed <= win_height else 0
