import sys


from SDL import SDL
from keys import keys
from person import person
from camera import camera
from tileEngine import tileEngine
from logicMap import logicMap
from collision import checkFloor, checkRoof, checkLeft, checkRight

from userTypes import aabb


# this is the width of your tiles
tileWidth, tileHeight = 32, 32


def main():

	# init the pySDL2 API
    sdl = SDL( 0, 0 )

    # print the screen res
    print(sdl.x, sdl.y)

    logic = logicMap("boxmap.csv", sdl.x, sdl.y, tileWidth, tileHeight)

    # make a camera 
    cam = camera( sdl.x, sdl.y )

    # set camera margins
    cam.margin.x = sdl.x//3
    cam.margin.y = sdl.y//3

    # create tile engine
    t = tileEngine( sdl )
    t.addTextMap( "boxmap.csv" )
    t.addTileSheet( "tileset.png" , tileWidth, tileHeight )

    # create a key set
    k = keys( sdl.setKeys( [ "up", "down", "left", "right" ] ) )

    # create a person
    side = 20

    # x, y, max_speed, acceleration, deceleration, width, height, dx=0, dy=0
    guy = person( 0., 0., 1000, 1000, 1000, side, side )

    box = aabb( 0, 0, tileWidth, tileHeight )
    boxRect = sdl.rect( box.x, box.y, tileWidth, tileHeight )

    # create an 'SDL_Rect' to render guy in
    rect = sdl.rect( guy.x, guy.y, guy.w, guy.h )

    
    sdl.setColor([0,255,0])
    
    GAME = True
    while GAME: # enter the main loop with the flag 'GAME'

        while sdl.eventLoop():   # event loop
            GAME = sdl.running() # quit if user presses 'esc' or clicks out
            k.poll( sdl.event )  # poll the keys

        # unpack the key flags
        guy.up, guy.down, guy.left, guy.right = k.unpack()

        # move guy!
        guy.move()

        # set the camera positions
        cam.move( guy.x, guy.y, guy.w, guy.h )

        logic.update(cam.x, cam.y)
           

        for i, o in enumerate( logic.register ):

            box.x, box.y = o[0]

            if o[1] > -1:

                if checkFloor( guy, box ):
                    guy.y = box.y - guy.h
                    guy.dy = 0

                if checkRoof( guy, box ):
                    guy.y = box.y + box.h
                    guy.dy = 0

                if checkLeft( guy, box ):
                    guy.x = box.x - guy.w
                    guy.dx = 0

                if checkRight( guy, box ):
                    guy.x = box.x + box.w
                    guy.dx = 0


        # set the position of the static rendering rect
        rect.x = int( guy.x  - cam.x )
        rect.y = int( guy.y  - cam.y )

        # paint the screen
        sdl.clearColor( [ 100, 0, 100 ] )

        # create layer
        t.addLayer( cam.x, cam.y, 0, 0 )

        # draw and clear the tile layers
        t.drawLayer(0)
        t.clearLayers()
        
        # draw the dude
        sdl.setColor( [ 0, 255, 255 ] )
        sdl.fillRect( rect )

        # flip the buffer!
        sdl.present()

    # destroy the window and renderer if user quits
    sdl.cleanUp()

if __name__ == "__main__":
    sys.exit( main() )
