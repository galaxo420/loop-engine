from euler import euler
from userTypes import *

class person():

    def __init__( self, x, y, max_speed, acceleration, deceleration, width, height, dx=0, dy=0 ):

        self.e = euler( acceleration, deceleration )

        self.x, self.y, self.dx, self.dy = x, y, dx, dy
        self.w, self.h = width, height
        self.max_speed = max_speed

        self.up, self.down, self.left, self.right = False, False, False, False
        
        self.old = point( self.x, self.y )

        
    def move( self ):

        # store x,y state (for collision checks)
        self.old.x, self.old.y = self.x, self.y

        # move the person according to user input
        if self.up ^ self.down:
            if self.up:
                self.y, self.dy = self.e.accelerate( self.y, self.dy, False)
            if self.down:
                self.y, self.dy = self.e.accelerate( self.y, self.dy, True)
        else:
            self.y, self.dy = self.e.decelerate( self.y, self.dy )

        if self.left ^ self.right:
            if self.left:
                self.x, self.dx = self.e.accelerate( self.x, self.dx, False)
            if self.right:
                self.x, self.dx = self.e.accelerate( self.x, self.dx, True)
        else:
            self.x, self.dx = self.e.decelerate( self.x, self.dx )

        # cap the velocity
        if self.dx > self.max_speed: self.dx = self.max_speed
        if self.dx < -self.max_speed: self.dx = -self.max_speed

        if self.dy > self.max_speed: self.dy = self.max_speed
        if self.dy < -self.max_speed: self.dy = -self.max_speed



    def stayOnScreen( self, left, right, top, bottom):
        if self.x < left:
            self.dx = 0
            self.x = left
        if self.x > right:
            self.dx = 0
            self.x = right

        if self.y < top:
            self.dy = 0
            self.y = top
        if self.y > bottom:
            self.dy = 0
            self.y = bottom

    def react( self, platform ):

        if platform.index == 0:

            self.y = platform.y - self.h
            self.dy = 0.

        elif platform.index == 1:

            self.x = platform.x - self.w
            self.dx = 0.

        elif platform.index == 2:

            self.y = platform.y
            self.dy = 0.

        elif platform.index == 3:

            self.x = platform.x
            self.dx = 0.