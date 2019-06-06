from ctypes import *
from sdl2 import *
from sdl2.sdlimage import IMG_LoadTexture

# API documentation (in C language) >>> https://wiki.libsdl.org/APIByCategory

class SDL:

	# init class with resolution (0, 0) for fullscreen at desktop resolution
    def __init__(self, screen_x, screen_y, window_text='', window_type=0):
        
        # initialize the pySDL2 API
        SDL_Init(SDL_INIT_EVERYTHING)

        if screen_x == 0 or screen_y == 0:	# desktop fullscreen

            self.dm = SDL_DisplayMode()
            SDL_GetDesktopDisplayMode(0, self.dm )
            self.x = self.dm.w
            self.y = self.dm.h
            window_type = SDL_WINDOW_FULLSCREEN

        else:								# user defined window dimensions
            self.x = screen_x
            self.y = screen_y

		# initialize SDL2 window, renderer and event manager

        self.window = SDL_CreateWindow( window_text.encode(), SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, self.x, self.y, window_type)
        self.renderer = SDL_CreateRenderer( self.window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC)
        self.event = SDL_Event()

        # set logical rendering size
        SDL_RenderSetLogicalSize( self.renderer, self.x, self.y)

	    # allow alpha blending for textures
        SDL_SetRenderDrawBlendMode( self.renderer, SDL_BLENDMODE_BLEND )

	    # show/hide cursor (0 to hide, 1 to show)
        SDL_ShowCursor(0)

	    # set the clip rect to the screen
        CLIP_RECT = SDL_Rect( 0, 0, self.x, self.y )
        SDL_RenderSetClipRect( self.renderer, CLIP_RECT )

	    # set the scale quality explicitly to nearest pixel interpolation
        SDL_SetHint( SDL_HINT_RENDER_SCALE_QUALITY, b"0" )

        # initialize the key dictionary (see bottom of file)
        self.setKeyDict()
     
    # load an image. returns a gpu texture
    def loadImage( self, file ):
        return IMG_LoadTexture( self.renderer, file.encode() )

    # return an SDL_Rect structure
    def rect( self, x, y, w, h):
        return SDL_Rect(int(x),int(y),int(w),int(h) )

    # render a gpu texture to the screen
    def render( self, texture, dest=None, source=None):
    	SDL_RenderCopy( self.renderer, texture, source, dest)


	# flip buffer (i.e., present the next frame)
    def present(self):
    	SDL_RenderPresent(self.renderer)

	# draw a filled SDL_Rect
    def fillRect(self, rect):
    	SDL_RenderFillRect(self.renderer, rect)

    # draw an SDL_Rect outline
    def drawRect(self, rect):
        SDL_RenderDrawRect(self.renderer, rect)

	# clear screen with a color
    def clearColor(self, color):
	    SDL_SetRenderDrawColor(self.renderer, color[0], color[1], color[2] , 255)
	    SDL_RenderClear(self.renderer)

	# set the render draw color
    def setColor(self, color):
	    SDL_SetRenderDrawColor(self.renderer, color[0], color[1], color[2] , 255)

	# returns true if game is running and false if user requests to quit or presses escape
    def running(self):
	    if self.event.type == SDL_QUIT or\
        (self.event.type == SDL_KEYDOWN and self.event.key.keysym.sym == SDLK_ESCAPE):
	        return False
	    else:
	        return True

    # this returns true if there are events in the event queue
    # it should be the condition for a nested 'while' loop
    # within the main loop in which you process user input
    def eventLoop( self ):
        if SDL_PollEvent( self.event ) != 0:
            return True
        else:
            return False

	# destroy the renderer and window
    def cleanUp(self):
	    SDL_DestroyRenderer(self.renderer)
	    SDL_DestroyWindow(self.window)

    # takes a list of keywords like "up" or "a" and returns a list
    # of corresponding SDL_KEYs like SDLK_UP or SDLK_a
    def setKeys( self, keys):
        nlist = []
        for k in keys:
            nlist.append( self.keyDict[k] )
        return nlist

    # prints a list of keywords for the keys (for debugging)
    def printKeyDict( self ):
        for i in self.keyDict.keys():
            print( i, end=', ' )
        print()

    # the keyboard dictionary is initialized
    def setKeyDict( self ):
        self.keyDict = {

            "up"    : SDLK_UP,
            "down"  : SDLK_DOWN,
            "left"  : SDLK_LEFT,
            "right" : SDLK_RIGHT,

            "a" : SDLK_a,
            "b" : SDLK_b,
            "c" : SDLK_c,
            "d" : SDLK_d,
            "e" : SDLK_e,
            "f" : SDLK_f,
            "g" : SDLK_g,
            "h" : SDLK_h,
            "i" : SDLK_i,
            "j" : SDLK_j,
            "k" : SDLK_k,
            "l" : SDLK_l,
            "m" : SDLK_m,
            "n" : SDLK_n,
            "o" : SDLK_o,
            "p" : SDLK_p,
            "q" : SDLK_q,
            "r" : SDLK_r,
            "s" : SDLK_s,
            "t" : SDLK_t,
            "u" : SDLK_u,
            "v" : SDLK_v,
            "w" : SDLK_w,
            "x" : SDLK_x,
            "y" : SDLK_y,
            "z" : SDLK_z

        }

        
