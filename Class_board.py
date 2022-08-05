import numpy as np
import operator
from Class_Pieces import *
import matplotlib.pyplot as plt
import copy

# The chess board is the main class of the code. It will allows to move the pieces etc.


#=======================================================================================================
# Generic notes
#=======================================================================================================
# The chess board class has only 1 (but important) attribute : self.board which is a dictionary of squares. Every square key is given as a coordinate tuple (x, y) where x, y € [0, ..., 7].
# The coordinate correspond to the chess notation as the following : (x, y) -> x + 1 = line (i.e the number); y + 1 = column (i.e. the letter). For e.g. (1, 2) is c2.
# Every self.board key leads to an instance of the "piece" class (see Class_Pieces.py) which means self.board[(x, y)] returns a black_pawn, a white_knight, an empty_piece etc.
# The class methods white_moves and black_moves are looping over all squares/pieces and return the full list of moves for the particular color where move format is a list of 2 tuples
# The method play_move(self, move) update self.board in the following way : the old square of the piece is replaced by an empty_piece instance while the new square become a copy of the old one.
# The method human_visualize give a view of the chess board in a more human friendly way
# The move_to_pgn method translate the moves ito the pgn format notation : e.g if knight [(1, 2), (3, 3)] -> Nd4 if d4 is empty or Nxd4 if d4 was occupied.







class chess_board :

	def __init__(self):
	
	# initialize the dict
	
		self.board = {}
		
	# Method that creates the dictionnary of pieces at the begining of the game. Everything is empty apart from the first lines of each camp which is full of pieces.
	def initialize(self) :
	
		for i in range(8) :
			for j in range(8):
				self.board[(i,j)] = empty_piece( (i,j) )
				
				
		for j in range(8) :
			self.board[(1, j)] = white_pawn( (1,j) )
			self.board[(6, j)] = black_pawn( (6,j) )
			
		self.board[(0,1)] = white_knight( (0,1) )
		self.board[(0,6)] = white_knight( (0,6) )
		self.board[(7,1)] = black_knight( (7,1) )
		self.board[(7,6)] = black_knight( (7,6) )
		
		self.board[(0,2)] = white_bishop( (0,2) )
		self.board[(0,5)] = white_bishop( (0,5) )
		self.board[(7,2)] = black_bishop( (7,2) )
		self.board[(7,5)] = black_bishop( (7,5) )
		
		self.board[(0,0)] = white_rook( (0,0) )
		self.board[(0,7)] = white_rook( (0,7) )
		self.board[(7,0)] = black_rook( (7,0) )
		self.board[(7,7)] = black_rook( (7,7) )
		
		self.board[(0,3)] = white_queen( (0,3) )
		self.board[(7,3)] = black_queen( (7,3) )
		
		self.board[(0,4)] = white_king( (0,4) )
		self.board[(7,4)] = black_king( (7,4) )
					
	
	# visualizing chessboard method		
	def human_visualize(self) :
	
		tab = np.empty((8,8), dtype = object)
		tab_color = np.empty((8,8), dtype = object)
		for i in range(8) :
			for j in range(8) :
				tab[i,j] = self.board[(7-i,j)].name
				if (i + j) % 2 == 0 :
					tab_color[i,j] = 'c'
				else : tab_color[i,j] = 'w'
		
		
		fig, ax = plt.subplots()
		table = ax.table(cellText=tab, cellColours=tab_color, loc='center')
		table.scale(1,3)
		ax.axis('off')
		plt.tight_layout()
		plt.show()
		
	
	#return all possible white moves (loop over all pieces, check if white, add all possible moves together, return a list of moves)	
	def white_moves(self) :
	
		all_white_moves = []
	
		for piece in self.board : 
			if self.board[piece].color == 'white':
				all_white_moves += self.board[piece].possible_moves(self.board)
				
		legal_moves_list = []
				
		for move in all_white_moves :
			if self.legal_move('white', move) : 
				legal_moves_list.append(move)


		return legal_moves_list
		
	
	# same as white moves but only used for the function legal moves that verify the checks. Need to be different to avoid infinite recursive	
	def white_moves_projection(self) :
	
		all_white_moves = []
	
		for piece in self.board : 
			if self.board[piece].color == 'white':
				all_white_moves += self.board[piece].possible_moves(self.board)
				
			
				
		return all_white_moves
		
	
	# similar to white_moves
	def black_moves(self) :
	
		all_black_moves = []
	
		for piece in self.board : 
			if self.board[piece].color == 'black':
				all_black_moves += self.board[piece].possible_moves(self.board)
				
		legal_moves_list = []
				
		for move in all_black_moves :
			if self.legal_move('black', move) : 
				legal_moves_list.append(move)


		return legal_moves_list
	
	# similar to white_moves_projection
	def black_moves_projection(self) :
	
		all_black_moves = []
	
		for piece in self.board : 
			if self.board[piece].color == 'black':
				all_black_moves += self.board[piece].possible_moves(self.board)
				
		return all_black_moves
		
	
	# actualize the board with the given move (replace old square piece by epty_piece and copy the piece to the new location + changing the piece attribute coordinate). Also check if len(move) ==3  => promotion of a pawn (see pawn classes for details). The third element is the type of promotion
	def play_move(self, move) :
	
		# take care of promotion if there is
		if len(move) == 3 :
			if move[2] == 'Q' :
				if self.board[move[0]].color == 'white' :
					self.board[move[0]] = white_queen(move[0])
				else :
					self.board[move[0]] = black_queen(move[0])
					
			if move[2] == 'N' :
				if self.board[move[0]].color == 'white' :
					self.board[move[0]] = white_knight(move[0])
				else :
					self.board[move[0]] = black_knight(move[0])
			if move[2] == 'R' :
				if self.board[move[0]].color == 'white' :
					self.board[move[0]] = white_rook(move[0])
				else :
					self.board[move[0]] = black_rook(move[0])
			if move[2] == 'B' :
				if self.board[move[0]].color == 'white' :
					self.board[move[0]] = white_bishop(move[0])
				else :
					self.board[move[0]] = black_bishop(move[0])
					
		# and then in any case move the piece
		self.board[move[0]].coordinate = move[1]
		self.board[move[1]] = self.board[move[0]]
		self.board[move[0]] = empty_piece(move[0])
		
			
	# translate a move into a pgn string format (like if N in (0,6) : [(0,6), (2, 5) ] -> 'Nf3'). return string. Needs the list of all playable moves to remove ambiguities		
	def move_to_pgn(self, move) :
		
		column_list = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h']
		all_moves_pgn = []
		
		
		pgn_move = ''
		
		piece_eaten = True
		# if piece_eaten = true -> add a 'x' to the notation
		if isinstance(self.board[move[1]], empty_piece) :
			piece_eaten = False
			# separate notation between pawns and the others
		if isinstance(self.board[move[0]], white_pawn) or isinstance(self.board[move[0]], black_pawn) :
			if piece_eaten :
				pgn_move = column_list[move[0][1]] + 'x' + column_list[move[1][1]] + str(move[1][0]+1)
				if len(move) == 3 :
					pgn_move += '=' + move[2]
			else :
				pgn_move = column_list[move[1][1]] + str(move[1][0]+1)
				if len(move) == 3 :
					pgn_move += '=' + move[2]
			
		else :
			letter = ''
			if isinstance(self.board[move[0]], white_knight) or isinstance(self.board[move[0]], black_knight) :
				letter = 'N'
			if isinstance(self.board[move[0]], white_bishop) or isinstance(self.board[move[0]], black_bishop) :
				letter = 'B'
			if isinstance(self.board[move[0]], white_rook) or isinstance(self.board[move[0]], black_rook) :
				letter = 'R'
			if isinstance(self.board[move[0]], white_queen) or isinstance(self.board[move[0]], black_queen) :
				letter = 'Q'
			if isinstance(self.board[move[0]], white_king) or isinstance(self.board[move[0]], black_king) :
				letter = 'K'
			
		
			if piece_eaten :
				pgn_move = letter + column_list[move[0][1]] + str(move[0][0]+1) + 'x' + column_list[move[1][1]] + str(move[1][0]+1)
			else : 
				pgn_move = letter + column_list[move[0][1]] + str(move[0][0]+1)  + column_list[move[1][1]] + str(move[1][0]+1)
					
			
			

		
					
		return pgn_move
		
		
		
		# Test the king legal moves : Create a copy of the board and test the move. Then check if any of the possible other player move reach the king square. If yes => not legal move and return False. If no, this is a legal move and returns True. This allows to take care of checking moves but also the king cannot suicide.
	def legal_move(self, player, move) :

		board_projection = copy.deepcopy(self)

		board_projection.play_move(move)
		
		king_position = (-1,-1)

			
		if player == 'white' :
		
			for square in board_projection.board :
				if isinstance(board_projection.board[square], white_king) :
					king_position = square
					

			if king_position in [x[1] for x in board_projection.black_moves_projection()] : 
				return False

			else :

				return True

				
				
		if player == 'black' :
			for square in board_projection.board :
				if isinstance(board_projection.board[square], black_king) :
					king_position = square
			
			if king_position in [x[1] for x in board_projection.white_moves_projection()] :
				return False

			else : 
				return True

					
		
		
		
		
		
		
		
		
		
		
		
		



		
	
		




 
