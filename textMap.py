'''
this class loads files that are like this:

"map.txt" :

0  0  0  0  0  0  0  0  
0  0  1  1  0  0  0  0  
0  1  1  1  1  1  0  0  
0  0  1  1  1  0  0  0  
0  0  0  0  0  0  0  0  
0  0  0  0  0  0  0  0  
2  2  2  2  2  2  2  2  
2  2  2  2  2  2  2  2

the class then calculates n and m and stores the data in
a one-dimensional list of integers ( called 'index' ) in 
the order that you would read them in english

methods:
	printData( self )
	printParameter( self, n, m, index )
	slice( self, x , y , n , m )

notes:
   n*m matrix: 

   1  0  0  0  1 -- n = 4
   0  1  0  0  0
   0  0  1  0  0
   |
   m = 3
'''

import csv

class textMap():

	def __init__( self, file ):

		# open file and read contents into 'self.index'
		f = open( file, 'r' )
		reader = csv.reader(f,delimiter = ",")
		self.index = list(reader)
		f.close() # don't forget to close!
		# find n and m
		self.n  = len(self.index[0])
		self.m = len(self.index)
		# de-nest the list
		self.index = [j for i in self.index for j in i]
		# cast to int
		self.index = [int(i) for i in self.index]


	# print all the data contained in the object (for debugging)
	def printSelf( self ):
		print("\nn = ", self.n, ", m = ", self.m, "\n", sep='')
		for i in range( len( self.index ) ):
			print( self.index[ i ], end='\t' )
			if (i+1)%self.n == 0:
			    print("\n")

	# print all the data handed to method (for debugging)
	def printArg( self, n, m, index ):
		if len(index) != n * m:
			return
		print("\nn = ", n, ", m = ", m, "\n", sep='')
		for i in range( len( index ) ):
			print( index[ i ], end='\t' )
			if (i+1)%n == 0:
			    print("\n")

	# returns a list containing a wrapped slice from the text map
	def slice(self, x , y , n , m ):

		''' x and y are the start coordinates of the map slice
			n and m are the dimensions of the list to be returned '''
		
		# take the modulus to find x and y on the map 
		x %= self.n
		y %= self.m

		# catch if either modulus are negative and if so stick them back on the map
		if ( x < 0 ) : x += self.n
		if ( y < 0 ) : y += self.m

		# set the current index to the start index position
		current = ( y * self.n ) + x

		# this is used to find the next index when the end of a slice-row is reached.
		''' do not attempt to simplify it by cancelling out 'self.n' because it
		    will remove the '//' operator and break the code '''
		sliceFactor = self.n * ( (x+n) // self.n + 1 ) - n

		# create a list to return
		nlist = []

		 # for the length of the slice...
		for i in range( n * m ):

	    	# append nlist with the current index then increment the current index
			nlist.append( self.index[ current ] )
			current += 1

			# if the index hits the end of the map-row, loop back the the start of the same map-row
			if current % self.n == 0:
				current -= self.n

			# if the next index hits the end of the slice-row, make sure it loops back correctly
			if (i+1)%n == 0: # 'i+1' is used rather than 'current' because we are interested in the slice position 
				current += sliceFactor # 'sliceFactor' is used here
				

			# if the index is out of range (i.e., off the bottom of the map), send it back to the top
			if current >= self.n * self.m:
				current -= self.n * self.m
		
		return nlist
