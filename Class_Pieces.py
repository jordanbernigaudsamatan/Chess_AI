import numpy as np
import operator

#=======================================================================================================
# Generic notes
#=======================================================================================================
# The pieces class are defined here. The main class is "pieces". Then 3 child class : "empty_piece", "white_piece", "black_piece" which differ only by color ("empty is a color").
# The empty_piece class -> for empty square on board.
# Then white_piece and black piece have children corresponding to specifics : "white_pawn", "black_pawn", "white_knight" etc.
# every one of these have a class method "possible_moves" which returns a list of possible moves (differ for each piece). The format of the move is a list of 2 tuples/coordinate : [ (x1, y1), (x2,y2) ] where the piece go to point 1 to 2.





# ============================================== Main classes ==========================================

# Define "Pieces" main class

class pieces :

	def __init__(self, coord, color = 'empty'):

		self.coordinate = coord
		self.color = color
		


# Define empty_piece class (which corresponds to empty square on board)

class empty_piece(pieces) :
	def __init__(self, coord, color = 'empty') :
		pieces.__init__(self, coord, color)
		self.name = ''
		
#Define white_piece class (assigns white color on top of pieces class)
		
class white_piece(pieces) :

	def __init__(self, coord, color = 'white') :
		pieces.__init__(self, coord, color)
		
#Define white_piece class (assigns black color on top of pieces class)

		
class black_piece(pieces) :

	def __init__(self, coord, color = 'black') :
		pieces.__init__(self, coord, color)
		
		

# ============================================== White pieces ==========================================	

		
		
		
		
#Define white_knight class	
class white_knight(white_piece) :

	def __init__(self, coord, color = 'white') :
		white_piece.__init__(self, coord, color)
		self.name = 'w_knight'

	# Move list of a knight
	def possible_moves(self, chessboard) :
		moves = []
		#define all possible directions for knight, loop over and test if square is accessible
		vector = [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2, 1), (-2,-1)]
		for vec in vector :
			if (tuple(map(operator.add, self.coordinate, vec)) in chessboard) :
				if not(chessboard[tuple(map(operator.add, self.coordinate, vec))].color == 'white') :
					moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, vec))] )
			
		
		return moves


# Define white_bishop class
class white_bishop(white_piece) :

	def __init__(self, coord, color = 'white') :
		white_piece.__init__(self, coord, color)
		self.name = 'w_bishop'

	# Move list of a bishop
	def possible_moves(self, chessboard) :
		moves = []
		#define all possible directions for bishop
		vector_direction = [(1,1), (1,-1), (-1,1), (-1,-1)]
		# loop over direction and loop over a x direction -> if empty : add move, if black piece add move + break the direction loop, if white piece break direction loop. Always test that square is in chessboard
		for direction in vector_direction :
			for i in range(1, 8) :
				vec = tuple([i * z for z in direction])
				if (tuple(map(operator.add, self.coordinate, vec)) in chessboard) :
					if chessboard[tuple(map(operator.add, self.coordinate, vec))].color == 'empty' :
						moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, vec))] )
					if chessboard[tuple(map(operator.add, self.coordinate, vec))].color == 'black' :
						moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, vec))] )
						break
					if chessboard[tuple(map(operator.add, self.coordinate, vec))].color == 'white' :
						break
		
		return moves
		

# Define white_rook class
class white_rook(white_piece) :

	def __init__(self, coord, color = 'white') :
		white_piece.__init__(self, coord, color)
		self.name = 'w_rook'
		self.can_castle = True

	# Move list of a bishop
	def possible_moves(self, chessboard) :
		moves = []
		#define all possible directions for rook
		vector_direction = [(0,1), (0,-1), (-1,0), (1,0)]
		# loop over direction and loop over a x direction -> if empty : add move, if black piece add move + break the direction loop, if white piece break direction loop. Always test that square is in chessboard
		for direction in vector_direction :
			for i in range(1, 8) :
				vec = tuple([i * z for z in direction])
				if (tuple(map(operator.add, self.coordinate, vec)) in chessboard) :
					if chessboard[tuple(map(operator.add, self.coordinate, vec))].color == 'empty' :
						moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, vec))] )
					if chessboard[tuple(map(operator.add, self.coordinate, vec))].color == 'black' :
						moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, vec))] )
						break
					if chessboard[tuple(map(operator.add, self.coordinate, vec))].color == 'white' :
						break
		
		return moves
		
		
# Define white_queen class
class white_queen(white_piece) :

	def __init__(self, coord, color = 'white') :
		white_piece.__init__(self, coord, color)
		self.name = 'w_queen'

	# Move list of a queen
	def possible_moves(self, chessboard) :
		moves = []
		#define all possible directions for rook
		vector_direction = [(0,1), (0,-1), (-1,0), (1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
		# loop over direction and loop over a x direction -> if empty : add move, if black piece add move + break the direction loop, if white piece break direction loop. Always test that square is in chessboard
		for direction in vector_direction :
			for i in range(1, 8) :
				vec = tuple([i * z for z in direction])
				if (tuple(map(operator.add, self.coordinate, vec)) in chessboard) :
					if chessboard[tuple(map(operator.add, self.coordinate, vec))].color == 'empty' :
						moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, vec))] )
					if chessboard[tuple(map(operator.add, self.coordinate, vec))].color == 'black' :
						moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, vec))] )
						break
					if chessboard[tuple(map(operator.add, self.coordinate, vec))].color == 'white' :
						break
		
		return moves





#Define white_king class	
class white_king(white_piece) :

	def __init__(self, coord, color = 'white') :
		white_piece.__init__(self, coord, color)
		self.name = 'w_king'
		self.can_castle = True

	# Move list of king
	def possible_moves(self, chessboard) :
		moves = []
		#define all possible directions for king, loop over and test if square is accessible
		vector = [(0,1), (0,-1), (-1,0), (1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
		for vec in vector :
			if (tuple(map(operator.add, self.coordinate, vec)) in chessboard) :
				if not(chessboard[tuple(map(operator.add, self.coordinate, vec))].color == 'white') :
					moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, vec))] )
		# Check 'O-0' castle possibility : check if squares are empty between king and rook + if roo here
		if self.can_castle :
			if chessboard[tuple(map(operator.add, self.coordinate, (0,1) ))].color == 'empty' and chessboard[tuple(map(operator.add, self.coordinate, (0,2) ))].color == 'empty' and isinstance(chessboard[tuple(map(operator.add, self.coordinate, (0,3) ))], white_rook) :
				if chessboard[tuple(map(operator.add, self.coordinate, (0,3) ))].can_castle :
					moves.append([self.coordinate, tuple(map(operator.add, self.coordinate, (0,2)))  ,  tuple(map(operator.add, self.coordinate, (0,3))), tuple(map(operator.add, self.coordinate, (0,1))) , 'O-O'])

		if self.can_castle:
			if chessboard[tuple(map(operator.add, self.coordinate, (0, -1)))].color == 'empty' and chessboard[tuple(map(operator.add, self.coordinate, (0, -2)))].color == 'empty' and isinstance(chessboard[tuple(map(operator.add, self.coordinate, (0, -3)))], white_rook):
				if chessboard[tuple(map(operator.add, self.coordinate, (0, -3)))].can_castle:
					moves.append([self.coordinate, tuple(map(operator.add, self.coordinate, (0, -2))), tuple(map(operator.add, self.coordinate, (0, -3))), tuple(map(operator.add, self.coordinate, (0, -1))), 'O-O-O'])

		return moves




# Define white_pawn class

# the promotion returns a different move format : for ex: [(6, 0) , (7 , 0)] => [(6, 0) , (7, 0), 'queen']

class white_pawn(white_piece) :

	def __init__(self, coord, color = 'white') :
		white_piece.__init__(self, coord, color)
		self.name = 'w_pawn'

	# Move list of a white pawn
	def possible_moves(self, chessboard) :
		moves = []
		promotion_type = ['Q', 'N', 'R', 'B']
		# move 1 : move by 2 square up if on the first line and empty squares above. Length of move = 4 because need to create a virtual pawn for take en passant
		if self.coordinate[0] == 1 :
			if chessboard[tuple(map(operator.add, self.coordinate, (2,0)))].color == 'empty' :
				if chessboard[tuple(map(operator.add, self.coordinate, (1,0)))].color == 'empty' :
					moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, (2,0))), 'create virtual', 'white'] )
		
		# move 2 : move by 1 square up if empty square above	
		if (tuple(map(operator.add, self.coordinate, (1,0))) in chessboard) :
			if chessboard[tuple(map(operator.add, self.coordinate, (1,0)))].color == 'empty' :
				if tuple(map(operator.add, self.coordinate, (1,0)))[0] == 7 :
					for promotion in promotion_type :
						moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, (1,0))), promotion] )
				else :
					moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, (1,0)))] )


		# move 3 : eat in one diagonal direction if black piece there			
		if (tuple(map(operator.add, self.coordinate, (1,1))) in chessboard) :		
			if  chessboard[tuple(map(operator.add, self.coordinate, (1,1)))].color == 'black' :
				if tuple(map(operator.add, self.coordinate, (1,1)))[0] == 7 :
					for promotion in promotion_type :
						moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, (1,1))), promotion] )
				else :
					moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, (1,1)))] )
		
		# move 4 : eat in the other diagonal direction if black piece there			
		if (tuple(map(operator.add, self.coordinate, (1,-1))) in chessboard) :	
			if chessboard[tuple(map(operator.add, self.coordinate, (1,-1)))].color == 'black':
				if tuple(map(operator.add, self.coordinate, (1,-1)))[0] == 7 :
					for promotion in promotion_type :
						moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, (1,-1))), promotion] )
				else :
					moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, (1,-1)))] )
					
		# move 5 : take "en passant" in one diagonal : Check if it exists a virtual pawn and add the possibility to eat it
		if (tuple(map(operator.add, self.coordinate, (1,-1))) in chessboard) :
			if isinstance( chessboard[tuple(map(operator.add, self.coordinate, (1,-1))) ], virtual_black_pawn) :
				moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, (1,-1))), 'destroy', 'black'] )
				
		# move 6 : take "en passant" in the other diagonal
		if (tuple(map(operator.add, self.coordinate, (1,1))) in chessboard) :
			if isinstance( chessboard[tuple(map(operator.add, self.coordinate, (1,1))) ], virtual_black_pawn) :
				moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, (1,1))) , 'destroy', 'black'])
		
		
		
			
		return moves
		

# Define virtual pawn for take en passant
class virtual_white_pawn(empty_piece) :

	def __init__(self, coord, color = 'empty') :
		empty_piece.__init__(self, coord, color)
		self.name = 'virtual_w_pawn'
		
	

		
# ============================================== Black pieces ==========================================

	

		

# Define black_knight class, see white one for details.
class black_knight(black_piece) :

	def __init__(self, coord, color = 'black') :
		black_piece.__init__(self, coord, color)
		self.name = 'b_knight'

	# Move list of a knight
	def possible_moves(self, chessboard) :
		moves = []
		vector = [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2, 1), (-2,-1)]
		for vec in vector :
			if (tuple(map(operator.add, self.coordinate, vec)) in chessboard) :
				if not(chessboard[tuple(map(operator.add, self.coordinate, vec))].color == 'black') :
					moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, vec))] )
			
		
		return moves	
		
		


		
# Define black_bishop class
class black_bishop(black_piece) :

	def __init__(self, coord, color = 'black') :
		black_piece.__init__(self, coord, color)
		self.name = 'b_bishop'


	def possible_moves(self, chessboard) :
		moves = []
		#define all possible directions for bishop
		vector_direction = [(1,1), (1,-1), (-1,1), (-1,-1)]
		for direction in vector_direction :
			for i in range(1, 8) :
				vec = tuple([i * z for z in direction])
				if (tuple(map(operator.add, self.coordinate, vec)) in chessboard) :
					if chessboard[tuple(map(operator.add, self.coordinate, vec))].color == 'empty' :
						moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, vec))] )
					if chessboard[tuple(map(operator.add, self.coordinate, vec))].color == 'white' :
						moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, vec))] )
						break
					if chessboard[tuple(map(operator.add, self.coordinate, vec))].color == 'black' :
						break
		
		return moves	
		
		
		
# Define black_rook class, see white one for details
class black_rook(black_piece) :

	def __init__(self, coord, color = 'black') :
		black_piece.__init__(self, coord, color)
		self.name = 'b_rook'
		self.can_castle = True


	def possible_moves(self, chessboard) :
		moves = []
		vector_direction = [(0,1), (0,-1), (-1,0), (1,0)]
		for direction in vector_direction :
			for i in range(1, 8) :
				vec = tuple([i * z for z in direction])
				if (tuple(map(operator.add, self.coordinate, vec)) in chessboard) :
					if chessboard[tuple(map(operator.add, self.coordinate, vec))].color == 'empty' :
						moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, vec))] )
					if chessboard[tuple(map(operator.add, self.coordinate, vec))].color == 'white' :
						moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, vec))] )
						break
					if chessboard[tuple(map(operator.add, self.coordinate, vec))].color == 'black' :
						break
		
		return moves	
		
		
		
# Define black_queen class, see white one for details
class black_queen(black_piece) :

	def __init__(self, coord, color = 'black') :
		black_piece.__init__(self, coord, color)
		self.name = 'b_queen'


	def possible_moves(self, chessboard) :
		moves = []
		vector_direction = [(0,1), (0,-1), (-1,0), (1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
		for direction in vector_direction :
			for i in range(1, 8) :
				vec = tuple([i * z for z in direction])
				if (tuple(map(operator.add, self.coordinate, vec)) in chessboard) :
					if chessboard[tuple(map(operator.add, self.coordinate, vec))].color == 'empty' :
						moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, vec))] )
					if chessboard[tuple(map(operator.add, self.coordinate, vec))].color == 'white' :
						moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, vec))] )
						break
					if chessboard[tuple(map(operator.add, self.coordinate, vec))].color == 'black' :
						break
		
		return moves	
		
		
		
		
#Define black_king class	
class black_king(black_piece) :

	def __init__(self, coord, color = 'black') :
		black_piece.__init__(self, coord, color)
		self.name = 'b_king'
		self.can_castle = True

	# Move list of king
	def possible_moves(self, chessboard) :
		moves = []
		#define all possible directions for king, loop over and test if square is accessible
		vector = [(0,1), (0,-1), (-1,0), (1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
		for vec in vector :
			if (tuple(map(operator.add, self.coordinate, vec)) in chessboard) :
				if not(chessboard[tuple(map(operator.add, self.coordinate, vec))].color == 'black') :
					moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, vec))] )


		if self.can_castle :
			if chessboard[tuple(map(operator.add, self.coordinate, (0,1) ))].color == 'empty' and chessboard[tuple(map(operator.add, self.coordinate, (0,2) ))].color == 'empty' and isinstance(chessboard[tuple(map(operator.add, self.coordinate, (0,3) ))], black_rook) :
				if chessboard[tuple(map(operator.add, self.coordinate, (0,3) ))].can_castle :
					moves.append([self.coordinate, tuple(map(operator.add, self.coordinate, (0,2)))  ,  tuple(map(operator.add, self.coordinate, (0,3))), tuple(map(operator.add, self.coordinate, (0,1))) , 'O-O'])

		if self.can_castle:
			if chessboard[tuple(map(operator.add, self.coordinate, (0, -1)))].color == 'empty' and chessboard[tuple(map(operator.add, self.coordinate, (0, -2)))].color == 'empty' and isinstance(chessboard[tuple(map(operator.add, self.coordinate, (0, -3)))], black_rook):
				if chessboard[tuple(map(operator.add, self.coordinate, (0, -3)))].can_castle:
					moves.append([self.coordinate, tuple(map(operator.add, self.coordinate, (0, -2))), tuple(map(operator.add, self.coordinate, (0, -3))), tuple(map(operator.add, self.coordinate, (0, -1))), 'O-O-O'])
			
		
		return moves	
		
		
		
		
# Define black_pawn class (See associate white_pawn class for details)

class black_pawn(black_piece) :

	def __init__(self, coord, color = 'black') :
		black_piece.__init__(self, coord, color)
		self.name = 'b_pawn'
		
		
	def possible_moves(self, chessboard) :
		moves = []
		promotion_type = ['Q', 'N', 'R', 'B']
		if self.coordinate[0] == 6 :
			if chessboard[tuple(map(operator.add, self.coordinate, (-2,0)))].color == 'empty' :
				if chessboard[tuple(map(operator.add, self.coordinate, (-1,0)))].color == 'empty' :
					moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, (-2,0))) , 'create virtual', 'black'] )
		
		if (tuple(map(operator.add, self.coordinate, (-1,0))) in chessboard) :
			if chessboard[tuple(map(operator.add, self.coordinate, (-1,0)))].color == 'empty' :
				if tuple(map(operator.add, self.coordinate, (-1,0)))[0] == 0 :
					for promotion in promotion_type :
						moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, (-1,0))), promotion] )
				else :
					moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, (-1,0)))] )
		
		if (tuple(map(operator.add, self.coordinate, (-1,1))) in chessboard) :		
			if  chessboard[tuple(map(operator.add, self.coordinate, (-1,1)))].color == 'white' :
				if tuple(map(operator.add, self.coordinate, (-1,1)))[0] == 0 :
					for promotion in promotion_type :
						moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, (-1,1))), promotion] )
				else :
					moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, (-1,1)))] )
		
		if (tuple(map(operator.add, self.coordinate, (-1,-1))) in chessboard) :	
			if chessboard[tuple(map(operator.add, self.coordinate, (-1,-1)))].color == 'white':
				if tuple(map(operator.add, self.coordinate, (-1,-1)))[0] == 0 :
					for promotion in promotion_type :
						moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, (-1,-1))), promotion] )
				else :
					moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, (-1,-1)))] )
					
		if (tuple(map(operator.add, self.coordinate, (-1,-1))) in chessboard) :
			if isinstance( chessboard[tuple(map(operator.add, self.coordinate, (-1,-1))) ], virtual_white_pawn) :
				moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, (-1,-1))), 'destroy', 'white'] )
				

		if (tuple(map(operator.add, self.coordinate, (-1,1))) in chessboard) :
			if isinstance( chessboard[tuple(map(operator.add, self.coordinate, (-1,1))) ], virtual_white_pawn) :
				moves.append( [self.coordinate, tuple(map(operator.add, self.coordinate, (-1,1))) , 'destroy', 'white'])
			
		return moves
		
		
		
# Similar to white virtual pawn
class virtual_black_pawn(empty_piece) :

	def __init__(self, coord, color = 'empty') :
		empty_piece.__init__(self, coord, color)
		self.name = 'virtual_b_pawn'	
		
		



		
	
		




 
