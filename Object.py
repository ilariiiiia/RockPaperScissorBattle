import math
import random


class Obj:
    def __init__(self, name, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y
        self.a = [0, 0]
        self.v = [0, 0]

    def __repr__(self):
        return f"name: {self.name}, x:{self.x}, y:{self.y};"

    def move(self, eat):
        # V3, with acceleration
        SCREENSIZE = 800
        FPS = 75
        MAXV = 180
        AMULT = 10
        tick = 1 / FPS
        target = self.nearest(eat)
        # sqrt(ax**2 + ay**2) = 1
        # and ax/dx = ay/dy
        # so ay = axdy/dx
        # so sqrt(ax**2+(axdy/dx)**2) = 1
        # take sqrt off
        # ax**2 + ax**2dy**2/dx**2 = 1
        # ax**2(1+dy**2/dx**2) = 1
        # ax**2 = 1/(1+dy**2/dx**2)
        # ax = sqrt(1/(1+dy**2/dx**2)
        # ay = axdy/dx
        try:
            k = ((target.y-self.y) ** 2)/((target.x - self.x) ** 2)
            self.a[0] = math.sqrt(1/(1+k))
            self.a[1] = self.a[0] * math.sqrt(k)
            self.a[0] *= AMULT if self.x < target.x else -AMULT
            self.a[1] *= AMULT if self.y < target.y else -AMULT
            # update velocity
            self.v[0] += self.a[0]
            self.v[1] += self.a[1]
            if self.v[0] > MAXV:
                self.v[0] = MAXV
            if self.v[1] > MAXV:
                self.v[1] = MAXV
            if self.v[0] < -MAXV:
                self.v[0] = -MAXV
            if self.v[1] < -MAXV:
                self.v[1] = -MAXV
            # update position
            self.x += self.v[0] * tick
            self.y += self.v[1] * tick
            if not SCREENSIZE > self.x > 0:
                self.v[0] *= -1
            if not SCREENSIZE > self.y > 0:
                self.v[1] *= -1
        except ZeroDivisionError:
            pass

        # if nearest is touched, kill it
        if -3 < self.x - target.x < 3 and -3 < self.y - target.y < 3:
            target.name = self.name

    def nearest(self, eatlist: list):
        x = self.x
        y = self.y

        def calcDistance(other: Obj):
            dist = math.sqrt((x - other.x) ** 2 + (y - other.y) ** 2)
            return dist

        res = []
        for d in eatlist:
            res.append(calcDistance(d))
        # get index of the nearest item
        try:
            i = res.index(min(res))
            return eatlist[i]
        except ValueError as e:
            # eatlist is out
            return Obj("", 400, 400)

    def combat(self, other):
        if self.name == other.name:
            return "Draw"
        if self.name == 'Rock':
            if other.name == "Paper":
                return "Lost"
            elif other.name == "Scissors":
                return "Won"
        elif self.name == "Paper":
            if other.name == "Rock":
                return "Won"
            elif other.name == "Scissors":
                return "Lost"
        else:
            if other.name == "Rock":
                return "Lost"
            return "Won"
