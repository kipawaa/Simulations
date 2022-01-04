import tkinter as tk
from random import seed, randint
from predator import Predator
from prey import Prey
from time import time_ns, sleep


WIN_WIDTH = 1650
WIN_HEIGHT = 1000

NUM_PREY = 30
NUM_PREDATORS = 10

def seedSim(userSeed=None):
    if userSeed:
        seed(userSeed)
    
    predators = [Predator(randint(0, WIN_WIDTH), randint(0, WIN_HEIGHT), 100, 100, 100, 7/10, 50) for i in range(NUM_PREDATORS)]
    prey = [Prey(randint(0, WIN_WIDTH), randint(0, WIN_HEIGHT), 100, 100, 100, 5/10, 30) for i in range(NUM_PREY)]

    return [predators, prey]


def updateCreatures(creatures, canvas):
    for species in creatures:
        for creature in species:
            creature.update(WIN_WIDTH, WIN_HEIGHT, creatures, canvas)
    

def drawCreatures(canvas, creatures):
    for species in creatures:
        for creature in species:
            creature.draw(canvas)


def runSim():
    root = tk.Tk()
    root.wm_title = ("Ecosystem")
    canvas = tk.Canvas(root, width=WIN_WIDTH, height=WIN_HEIGHT)
    canvas.grid(row=0, column=0)

    # seed everything here
    creatures = seedSim()


    while (True):
        # frame start time
        frame_time = time_ns()
        
        # remove all drawings
        canvas.delete("all")

        # update positions and counts etc
        updateCreatures(creatures, canvas)

        # draw things
        drawCreatures(canvas, creatures)

        # update canvas
        canvas.update()

        # wait until at least 0.02s has passed to draw next frame (approx 60 frames/second)
        sleep(0.02 - (frame_time - time_ns())/1000000000)

    mainloop()
    root.destroy()


if __name__ == "__main__":
    runSim()
