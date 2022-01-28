import pygame as pg
import random

def circle():
    global grow, radius
    radius = radius + 1 if grow else radius - 1
    if radius > 100:
        grow = 0
    if radius < 10:
        grow = 1
    # create random rgb values
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)

    # (screen, rgb, x y coordinates, radius)
    pg.draw.circle(screen,
        (r,g, b),
        (100, 150),
        radius)


def listen():
    """ quit the window when user presses the red x button of the window """
    [pg.quit() for event in pg.event.get() if event.type == pg.QUIT]

def mainloop():
    """ This function runs until users quit the window """
    global grow
    grow = 1
    while True:
        listen() # this calls the function to quit the window
        screen.fill(0)
        circle() # This will call the animation
        clock.tick(20)
        pg.display.update()


pg.init()
radius = 100
screen = pg.display.set_mode((200, 300))
clock = pg.time.Clock()
mainloop()
