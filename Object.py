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
        print("eat after being passed to the function", eat)
        print("self in the function?", self)
        # V3, with acceleration
        ax = self.a[0]
        ay = self.a[1]
        SCREENSIZE = 800
        FPS = 75
        tick = 1 / FPS
        if self.x < 0:
            ax += 1
            x = False
        elif self.x > SCREENSIZE:
            ax -= 1
            x = False
        else:
            x = True
        if self.y < 0:
            ay += 1
            y = False
        elif self.y > SCREENSIZE:
            ay -= 1
            y = False
        else:
            y = True
        if y and x:
            ax = random.randint(0, 50)
            ay = random.randint(0, 50)
            near = self.nearest(eat)
            if not y:
                # only x
                ax *= (near.x > self.x)
            elif not x:
                # only y
                ay *= (near.y > self.y)
            else:
                # both
                ax *= (near.x > self.x)
                ay *= (near.y > self.y)
        self.a = [ax, ay]
        self.v[0] += ax * tick
        self.v[1] += ay * tick
        self.x += self.v[0] * tick + (ax*tick**2)/2
        self.y += self.v[1] * tick + (ay * tick ** 2) / 2

    def nearest(self, eatlist):
        x = self.x
        y = self.y

        def calcDistance(other):
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
            print(e)
            print("Error occurred, returning random one")
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
