from textMap import textMap
from userTypes import *

'''
			the 'logicMap' class is centred around a list called 'register'.

			each position in 'register' contains information about a position
			and a logic index. register[i][0] holds a tuple containing an integer
			multiple of the tile width and tile height respectively, which is the
			(x,y) position of the i-th tile. register[i][1] holds an integer
			value for a logic index which denotes how that tile behaves.

			of the tile

'''


class logicMap () :
	def __init__( self, file, camWidth, camHeight, tileWidth, tileHeight ):
		
		# camera dimensions
		self.camWidth, self.camHeight = camWidth, camHeight

		# tile object
		self.tile = aabb( 0, 0, tileWidth, tileHeight )

		# logical map
		self.logic = textMap( file )

		# a point structure to hold cam.x % tile.w ...
		self.phase = point( 0, 0 )

		# set the number of tiles to be checked plus dimensions
		self.row = ( self.camWidth // self.tile.w ) + 1
		self.col = ( self.camHeight // self.tile.h ) + 1
		self.count = self.row * self.col

		# init the register
		self.register = [ 0 ] * self.count

	def update( self, x, y ):

		# set the phase
		self.phase.x = x % self.tile.w
		self.phase.y = y % self.tile.h

		# initial tile position
		self.tile.x = x - self.phase.x
		self.tile.y = y - self.phase.y

		# take the relevent slice of the logic map
		self.nlist = self.logic.slice(self.tile.x//self.tile.w, self.tile.y//self.tile.h,self.row,self.col)

		rowCounter = 0

		for i in range( self.count ) :
			# add the (x.y) position and logic index to the register
			temp = [ ( self.tile.x, self.tile.y ), self.nlist[ i ] ]
			self.register[ i ] = temp
			# update the tile position
			self.tile.x += self.tile.w

			rowCounter += 1
			if rowCounter%self.row == 0:
				self.tile.x = x - self.phase.x
				self.tile.y += self.tile.h

