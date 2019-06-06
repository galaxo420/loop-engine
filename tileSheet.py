from sdl2 import *

class tileSheet():

    def __init__( self, sdl, file, tileWidth, tileHeight ):
        
        # grab some methods/data from the main sdl instance 
        self.render = sdl.render
        self.fillRect = sdl.fillRect # may want this for debugging
        self.screen_x = sdl.x
        self.screen_y = sdl.y

        # save the initialization arguments
        self.texture = sdl.loadImage( file )
        self.tileWidth = tileWidth
        self.tileHeight = tileHeight

        # create some rects for rendering
        self.source = sdl.rect( 0, 0, self.tileWidth, self.tileHeight )
        self.dest = sdl.rect( 0, 0, self.tileWidth, self.tileHeight )

        # get the size of the texture in pixels
        self.sheetWidth, self.sheetHeight = c_int(0), c_int(0) # SDL_QueryTexture requires c_int type
        SDL_QueryTexture( self.texture , None , None , self.sheetWidth , self.sheetHeight )
        # cast 'self.sheetWidth' and 'self.sheetHeight' to Python int
        self.sheetWidth, self.sheetHeight = self.sheetWidth.value, self.sheetHeight.value

        # calculate the number of source tiles
        self.sourceRow = (self.sheetWidth // self.tileWidth)
        self.sourceCount = self.sourceRow * (self.sheetHeight // self. tileHeight)

        # calculate the number of destination tiles
        overSpill = 3
        self.destRow = (self.screen_x // self.tileWidth) + overSpill
        self.destCount = self.destRow * ( (self.screen_y // self. tileHeight) + overSpill )

        # define a list of tuples for the clip position of the source rect
        temp_x, temp_y = 0, 0
        self.source_position = []
        for i in range( self.sourceCount ):

            self.source_position.append( ( temp_x, temp_y ) )

            temp_x += self.tileWidth

            if (i+1)%self.sourceRow == 0:
                temp_x = 0
                temp_y += self.tileHeight

        # define a list of tuples for the position of the destination rect
        temp_x, temp_y = -self.tileWidth, -self.tileHeight
        self.dest_position = []
        for i in range( self.destCount ):

            self.dest_position.append( ( temp_x, temp_y ) )

            temp_x += self.tileWidth

            if (i+1)%self.destRow == 0:
                temp_x = -self.tileWidth
                temp_y += self.tileHeight


    def draw( self, index, x_offset, y_offset):

        if len(index) != self.destCount:
            return

        for i in range( self.destCount ):

            if index[i] == -1: continue

            self.source.x, self.source.y = self.source_position[ index[i] ][0], self.source_position[ index[i] ][1]
            self.dest.x, self.dest.y = self.dest_position[i][0] + x_offset, self.dest_position[i][1] + y_offset
            self.render( self.texture, self.dest, self.source )

