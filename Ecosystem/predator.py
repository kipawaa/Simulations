from creature import Creature
from math import dist

class Predator(Creature):
    def findFood(self, preyList):
        closestPrey = min([(dist((self.x, self.y), (prey.x, prey.y)), prey) \
                for prey in preyList], key=lambda x:x[0])

        prey = closestPrey[0]
        distance = closestPrey[1]
        
        self.direction = ((self.x - prey.x) / distance, (self.y - prey.y) / distance)
