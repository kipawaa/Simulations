from creature import Creature
from random import random
from math import pi, sin, cos

class Prey(Creature):
    
    def draw(self, canvas):
        canvas.create_oval(self.x - 5, self.y - 5, self.x + 5, self.y + 5, fill="black")

    def update(self, win_width, win_height):
        # change the direction by up to pi/6
        self.direction += (2 * random() - 1) * pi / 6
        self.x += cos(self.direction) if 0 <= self.x + cos(self.direction) <= win_width else 0
        self.y += sin(self.direction) if 0 <= self.y + sin(self.direction) <= win_height else 0
