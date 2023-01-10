import random

import pygame

from Obj import Obj as Object


def rock(t=(0, 0)):
    return Object("Rock", t[0], t[1])


def paper(t=(0, 0)):
    return Object("Paper", t[0], t[1])


def scissors(t=(0, 0)):
    return Object("Scissors", t[0], t[1])


SCREENSIZE = 400
OBJRADIUS = 3

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)


def randomGenCoord():
    return random.randint(0, SCREENSIZE), random.randint(0, SCREENSIZE)


def main():
    objs = []
    n = 50
    # prepare the objects
    for _ in range(n):
        for a in [
            rock(randomGenCoord()),
            paper(randomGenCoord()),
            scissors(randomGenCoord())
        ]:
            objs.append(a)
    # objects prepared
    # now set up the screen
    SCREEN = pygame.display.set_mode((SCREENSIZE, SCREENSIZE))
    while True:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

        for a in objs:
            c = RED if a.name == "Rock" else BLUE if a.name == "Scissors" else GREEN
            pygame.draw.circle(SCREEN, c, (a.x, a.y), OBJRADIUS)
            a.move()
        pygame.display.update()


if __name__ == "__main__":
    main()
