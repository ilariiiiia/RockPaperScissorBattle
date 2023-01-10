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
    a = l
    return list(filter(lambda x: x.name == "Rock", a))


def filterPapers(l):
    a = l
    return list(filter(lambda x: x.name == "Paper", a))


def filterScissors(l):
    a = l
    return list(filter(lambda x: x.name == "Scissors", a))


SCREENSIZE = 800
OBJRADIUS = 3

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)


def randomGenCoord():
    return random.randint(0, SCREENSIZE), random.randint(0, SCREENSIZE)


def main():
    clock = pygame.time.Clock()
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

        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

        # show and move objects
        for a in objs:
            color = RED if a.name == "Rock" else BLUE if a.name == "Scissors" else GREEN
            pygame.draw.circle(SCREEN, color, (a.x, a.y), OBJRADIUS)
            # draw velocity lines
            # pygame.draw.line(SCREEN, WHITE, (a.x, a.y), (a.x + (a.v[0])*2, a.y + (a.v[1])*2))
            # pygame.draw.line(SCREEN, RED, (a.x, a.y), (a.x + (a.a[0]) * 10, a.y + (a.a[1]) * 10))
            # draw target
            # pygame.draw.circle(SCREEN, WHITE, (400, 400), OBJRADIUS + 2)
            if a.name == "Rock":
                eat = filterScissors(objs)
            elif a.name == "Scissors":
                eat = filterPapers(objs)
            else:
                eat = filterRocks(objs)
            a.move(eat)

        # update screen
        pygame.display.flip()
        clock.tick(150)


if __name__ == "__main__":
    main()
