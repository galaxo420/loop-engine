from sdl2 import *

class keys():

	# init class with an ordered list of 'SDL_KEY's ( e.g., SDLK_UP or SDLK_w )
    def __init__( self, nlist ):
        self.nlist = nlist # nlist holds the list of 'SDL_KEY's
        self.key = [] # key holds the boolian flags that correspond to each key
        for i in range( len( nlist ) ):
        	self.key.append( False )

        self.keyCount = len( self.key )

    # returns a list of 'False's that is the length of the keyset
    def setFlags( self ):
    	return [ False for i in range( self.keyCount ) ]

    # set key flags according to SDL_Event instance
    def poll( self, event ):
        for i in range( len( self.nlist ) ):
        	if event.type == SDL_KEYDOWN:
        		if event.key.keysym.sym == self.nlist[ i ]:
        			self.key[ i ] = True
        	if event.type == SDL_KEYUP:
        		if event.key.keysym.sym == self.nlist[ i ]:
        			self.key[ i ] = False

    # return a list of the current key flags
    def unpack( self ):
    	return self.key

