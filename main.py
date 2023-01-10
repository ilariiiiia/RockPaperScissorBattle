import random

import pygame

from Object import Obj as Object


def rock(t=(0, 0)):
    return Object("Rock", t[0], t[1])


def paper(t=(0, 0)):
    return Object("Paper", t[0], t[1])


def scissors(t=(0, 0)):
    return Object("Scissors", t[0], t[1])


def filterRocks(l):
    # filters l to Rock-only Objects
    a = l
    return list(filter(lambda x: x.name == "Rock", a))


def filterPapers(l):
    # filters l to Papers-only Objects
    a = l
    return list(filter(lambda x: x.name == "Paper", a))


def filterScissors(l):
    # filters l to Scissors-only Objects
    a = l
    return list(filter(lambda x: x.name == "Scissors", a))


# CONSTANTS

SCREENSIZE = 800
FPS = 150
OBJRADIUS = 3  # radius of the spheres
DEBUG = False

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
SCREEN = pygame.display.set_mode((SCREENSIZE, SCREENSIZE))


def randomGenCoord() -> (int, int):
    # returns a random coordinate with x and y between 0 and screensize
    return random.randint(0, SCREENSIZE), random.randint(0, SCREENSIZE)


def debug(a: Object, speed=True, acc=True, center=True):
    # function to be added into the for loop inside the main loop for debug purposes.
    # each of the optional parameters shows some info about the object a.
    # speed shows the speed vector
    # acc shows the acceleration vector
    # center shows the center of the screen (where the objects will go if they have nothing to eat)
    SPMULT = 2  # multiplier for speed
    ACCMULT = 10  # multiplier for acceleration
    XRAD = 2  # extra radius for the screen center
    if speed:
        pygame.draw.line(SCREEN, WHITE, (a.x, a.y), (a.x + (a.v[0]) * SPMULT, a.y + (a.v[1]) * SPMULT))
    if acc:
        pygame.draw.line(SCREEN, RED, (a.x, a.y), (a.x + (a.a[0]) * ACCMULT, a.y + (a.a[1]) * ACCMULT))
    if center:
        pygame.draw.circle(SCREEN, WHITE, (SCREENSIZE / 2, SCREENSIZE / 2), OBJRADIUS + XRAD)


def main():
    clock = pygame.time.Clock()
    objs = []
    n = 50
    # prepare the objects
    for _ in range(n):
        for point in [
            rock(randomGenCoord()),
            paper(randomGenCoord()),
            scissors(randomGenCoord())
        ]:
            objs.append(point)
    while True:
        SCREEN.fill(BLACK)

        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

        # show and move objects
        for point in objs:

            color = RED if point.name == "Rock" else BLUE if point.name == "Scissors" else GREEN

            pygame.draw.circle(SCREEN, color, (point.x, point.y), OBJRADIUS)
            if DEBUG:
                debug(point, speed=True, acc=True, center=True)

            if point.name == "Rock":
                eat = filterScissors(objs)
            elif point.name == "Scissors":
                eat = filterPapers(objs)
            else:
                eat = filterRocks(objs)
            point.move(eat)

        # update screen
        pygame.display.flip()
        clock.tick(150)


if __name__ == "__main__":
    main()
