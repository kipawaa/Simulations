import tkinter as tk
from random import seed, randint
from prey import Prey

WIN_WIDTH = 1650
WIN_HEIGHT = 1000

NUM_PREY = 10

def seedSim(userSeed=None):
    if userSeed:
        seed(userSeed)
    
    prey = [Prey(randint(0, WIN_WIDTH), randint(0, WIN_HEIGHT), 100, 100, 100, 5, 12) for i in range(NUM_PREY)]

    return prey


def updateCreatures(creatures):
    for creature in creatures:
        creature.update(WIN_WIDTH, WIN_HEIGHT)
    

def drawCreatures(canvas, creatures):
    for creature in creatures:
        creature.draw(canvas)


def runSim():
    root = tk.Tk()
    root.wm_title = ("Ecosystem")
    canvas = tk.Canvas(root, width=WIN_WIDTH, height=WIN_HEIGHT)
    canvas.grid(row=0, column=0)

    # seed everything here
    prey = seedSim()

    while (True):
        # remove all drawings
        canvas.delete("all")

        # update positions and counts etc
        updateCreatures(prey)

        # draw things
        drawCreatures(canvas, prey)

        # update canvas
        canvas.update()
    mainloop()
    root.destroy()


if __name__ == "__main__":
    runSim()
