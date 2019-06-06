from textMap import textMap
from tileSheet import tileSheet

class tileEngine():

	def __init__( self, sdl ):
		
		self.sdl = sdl

		self.txt = []
		
		self.tile = []
		self.n = []
		self.m = []

		self.layer = []


	def addTextMap( self, file ):
		self.txt.append( textMap( file ) )

	def addTileSheet( self, file, tileWidth, tileHeight ):
		i = len( self.tile )
		self.tile.append( tileSheet( self.sdl, file, tileWidth, tileHeight ) )
		self.n.append( self.tile[i].destRow )
		self.m.append( self.tile[i].destCount//self.tile[i].destRow )

	def addLayer( self, x, y, mapIndex, tileIndex, phase=1. ):

		# grab a slice for the map to be rendered
		''' this needs the '-1' to compensate for the tiles being drawn in a -1 tile position. '''
		nslice = self.txt[ mapIndex ].slice( x // self.tile[ tileIndex ].tileWidth  - 1 ,
										     y // self.tile[ tileIndex ].tileHeight - 1 ,
										     self.n[ tileIndex ],
										     self.m[ tileIndex ] )

		x_offset = -( x % self.tile[ tileIndex ].tileWidth  )
		y_offset = -( y % self.tile[ tileIndex ].tileHeight )

		self.layer.append( [ tileIndex, nslice, x_offset, y_offset ] )

	def clearLayers( self ):
		self.layer = []

	def drawLayer( self, layerIndex ):

		self.tile[ self.layer[ layerIndex ][ 0 ] ].draw( self.layer[ layerIndex ][ 1 ],
			                   							 self.layer[ layerIndex ][ 2 ],
							   							 self.layer[ layerIndex ][ 3 ] )


