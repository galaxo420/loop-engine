from euler import euler
from userTypes import *

class camera():

	def __init__( self, screen_x, screen_y ):

		self.x, self.y = 0.0, 0.0
		self.dx, self.dy = 0.0, 0.0
		self.w, self.h = screen_x, screen_y
		self.margin = point( self.w//4, self.h//4)
		self.e = euler( 0.0, 0.0 )


	def getCameraPosition( self ):
		return self.x, self.y


	def centreLocked( self, x, y, w, h):

		self.x = int(x) + w//2 - self.w//2
		self.y = int(y) + h//2 - self.h//2



	def move( self, x, y, w, h):

		x, y = int(x), int(y) 
		if self.x < x + w - self.w + self.margin.x:
			self.x = x + w - self.w + self.margin.x
		if self.x > x - self.margin.x:
			self.x = x - self.margin.x
		if self.y < y + h - self.h + self.margin.y:
			self.y = y + h - self.h + self.margin.y
		if self.y > y - self.margin.y:
			self.y = y - self.margin.y

