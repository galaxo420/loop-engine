
class euler():

    def __init__( self, acceleration, deceleration, dt=1./60.):

        self.acceleration = acceleration
        self.deceleration = deceleration
        self.dt = dt
        self.last_v = 0

    
    def accelerate( self, x, dx, isPositive ):

        self.last_v = dx

        if isPositive: 
            sign = 1
        else:
            sign = -1

        dx += sign * self.acceleration * self.dt
        x += ( dx + self.last_v ) * 0.5 * self.dt

        return x, dx


    def decelerate( self, x, dx ):

        ellipsis = self.deceleration * self.dt

        if ( dx > ellipsis) or ( dx < -ellipsis ):

            self.last_v = dx

            if dx < -ellipsis:

                dx += self.deceleration * self.dt
                x += (dx + self.last_v) * 0.5 * self.dt
            
            if dx > ellipsis:

                dx -= self.deceleration * self.dt
                x += (dx + self.last_v) * 0.5 * self.dt        
        else:
            dx = 0

        return x, dx
