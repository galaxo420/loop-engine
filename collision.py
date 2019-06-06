'''
these three functions are for collision detection using 'axis aligned normals'

normal =        x    x------------x+w
                |
                |
                |
                |
                |
               x+w

'''

''' 
		the 'index' in the 'platform' class works like this:

			the indeces are in sets of four. each set of 
			four is 'floor, right wall, roof, left wall'.

			the 'player' class has a 'react()' function to
			deal with each platform type, and the detection routine
			will decide where to check based platform.index%4

'''

# checks if the player is projecting on the platform
def checkLine( player_x, platform_x, player_width, platform_width ):
    if ( player_x + player_width > platform_x ) and ( player_x < platform_x + platform_width ):
        return True
    else:
        return False

# checks if a collision has occured with the player moving in the positive direction
def checkPositive( new_y, old_y, platform_y ):
    if ( old_y <= platform_y ) and ( new_y > platform_y ):
        return True
    else:
        return False

# checks if a collision has occured with the player moving in the negative direction
def checkNegative( new_y, old_y, platform_y ):
    if ( old_y >= platform_y ) and ( new_y < platform_y ):
        return True
    else:
        return False
	

def checkFloor( person, platform ) :

	# is the player above or below the platform
	if checkLine( person.x , platform.x, person.w, platform.w ):
	    # has the player hit the floor
	    if checkPositive( person.y + person.h, person.old.y + person.h, platform.y ):
	       return True
	return False

def checkRoof( person, platform ) :

	# is the player above or below the platform
	if checkLine( person.x , platform.x, person.w, platform.w ):
    	# has the player hit the roof
	    if checkNegative( person.y, person.old.y, platform.y + platform.h ):
	        return True

def checkLeft( person, platform ) :

	# is the player to the left or right of the platform
	if checkLine( person.y, platform.y, person.h, platform.w ):
	    # has the player hit the left side of the platform
	    if checkPositive( person.x + person.w, person.old.x + person.w, platform.x ):
	    	return True
	return False

def checkRight( person, platform ) :
	# is the player to the left or right of the platform
	if checkLine( person.y, platform.y, person.h, platform.w ):
	    # has the player hit the right side of the platform
	    if checkNegative( person.x, person.old.x, platform.x + platform.w ):
	        return True
	return False

