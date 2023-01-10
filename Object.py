import math  # used for sqrt


class Obj:
    def __init__(self, name, x=0, y=0):
        """
        An Object, also called point

        :param name: String, either "Rock", "Paper", or "Scissors"
        :param x: the x center of the point
        :param y: the y center of the point
        """
        self.name = name
        self.x = x
        self.y = y
        self.a = [0, 0]  # acceleration vector
        self.v = [0, 0]  # velocity vector

    def __repr__(self):
        return f"name: {self.name}, x:{self.x}, y:{self.y}, v:{self.v}, a:{self.a};"

    def move(self, eat):
        """
        Makes the Object decide its next move by setting acceleration values.

        :param eat: list of other Objects that self can eat
        :return: Nothing
        """
        # Constants
        SCREENSIZE = 800
        FPS = 150
        MAXV = 180  # Maximum velocity
        AMULT = 10  # Multiplier for acceleration
        DIST2KILL = 3  # Distance to which other Objects have to be to be "killed"
        tick = 1 / FPS  # tick time

        target = self.nearest(eat)
        """
        Here follows a bunch of math to understand how I calculated the two acceleration components. I wanted them to
        be in such a way that the resultant sum vector was of length one. Hence sqrt(ax^2 + ay^2) = 1. Calculations
        follow:
        sqrt(ax^2 + ay^2) = 1
        and ax/dx = ay/dy
        so ay = axdy/dx
        so sqrt(ax^2+(axdy/dx)^2) = 1
        take sqrt off (square both sides)
        ax**2 + ax^2*dy^2/dx^2 = 1
        ax**2(1+dy^2/dx^2) = 1
        ax**2 = 1/(1+dy^2/dx^2)
        ax = sqrt(1/(1+dy^2/dx^2)
        ay = axdy/dx
        for brevity and clarity sake, let t = dy/dx and let k = t^2
        """
        try:  # see except to understand why
            t = (target.y - self.y) / (target.x - self.x)
            k = t ** 2
            self.a[0] = math.sqrt(1 / (1 + k))
            self.a[1] = self.a[0] * t
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
        except ZeroDivisionError:  # this happens if target.x == self.x. In that case, don't accelerate the Object
            pass

        # if nearest prey is touched, transform it into an ally
        if -DIST2KILL < self.x - target.x < DIST2KILL and -DIST2KILL < self.y - target.y < DIST2KILL:
            target.name = self.name

    def nearest(self, eatlist: list):
        """
        Returns the nearest object in eatlist from self

        :param eatlist: list of Obj's
        :return: Obj
        """

        # Constant
        SCREENSIZE = 800

        x = self.x
        y = self.y

        def calcDistance(other: Obj):  # helper
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
            # eatlist is empty, make the Object go to the center
            return Obj("", SCREENSIZE//2, SCREENSIZE//2)
