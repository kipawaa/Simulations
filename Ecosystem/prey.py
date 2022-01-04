from creature import Creature
from random import random
from math import dist, pi, sin, cos, atan2
from time import time_ns

class Prey(Creature):
    
    def draw(self, canvas):
        canvas.create_oval(self.x - 5, self.y - 5, self.x + 5, self.y + 5, fill="black")

    def update(self, win_width, win_height, creatures, canvas):
        # find nearest mate
        mate = min([(dist((self.x, self.y), (mate.x, mate.y)), mate) for mate in creatures[1] if mate is not self])

        # find nearest predator
        predator = min([(dist((self.x, self.y), (predator.x, predator.y)), predator) for predator in creatures[0]])

        # if we see a predator then run
        if predator[0] < self.sightRange:
            self.direction = -atan2(predator[1].y - self.y, predator[1].x - self.x)
        # if we see a mate then go to them
        elif mate[0] < self.sightRange and time_ns() - self.breedTime > 10000000000:
            #canvas.create_line((self.x, self.y), (mate[1].x, mate[1].y), fill="green")
            if mate[0] < 2.5:
                creatures[1].append(Prey(self.x, self.y, 100, 100, 100, 5/10, 30))
                self.breedTime = time_ns()
                mate[1].breedTime = time_ns()
                print("baby!")
            self.direction = atan2(mate[1].y - self.y, mate[1].x - self.x)
        # otherwise wander aimlessly
        else:
            # change the direction by up to pi/12
            self.direction += (2 * random() - 1) * pi / 6
        
        self.x += cos(self.direction) * self.speed if 0 <= self.x + cos(self.direction) * self.speed <= win_width else 0
        self.y += sin(self.direction) * self.speed if 0 <= self.y + sin(self.direction) * self.speed <= win_height else 0
