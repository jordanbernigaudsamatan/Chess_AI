import numpy as np
import operator
from Class_Pieces import *
import matplotlib.pyplot as plt
import copy
from typing import Tuple
import torch
import torch.nn.functional as Fn
import chess
import chess.pgn
from io import StringIO
import re

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







class ChessBoard :

	def __init__(self):
	
	# initialize the dict and column + line index list
	
		self.board = {}
		self.linelist = ['1', '2', '3', '4', '5', '6', '7', '8']
		self.columnlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
		self.pgn_string = ""
		self.round = 1

	# Method that creates the dictionnary of pieces at the begining of the game. Everything is empty apart from the first lines of each camp which is full of pieces.
	def initialize(self) :
		self.white_to_play = True
		for i in range(8) :
			for j in range(8):
				self.board[(i,j)] = EmptyPiece( (i,j) )
				
				
		for j in range(8) :
			self.board[(1, j)] = WhitePawn( (1,j), 'wP'+self.columnlist[j]+'2' )
			self.board[(6, j)] = BlackPawn( (6,j) , 'bP'+self.columnlist[j]+'7')
			
		self.board[(0,1)] = WhiteKnight( (0,1) , 'wNb1')
		self.board[(0,6)] = WhiteKnight((0,6) ,  'wNg1' )
		self.board[(7,1)] = BlackKnight( (7,1), 'bNb8' , )
		self.board[(7,6)] = BlackKnight( (7,6), 'bNg8' )
		
		self.board[(0,2)] = WhiteBishop( (0,2), 'wBc1'  )
		self.board[(0,5)] = WhiteBishop( (0,5), 'wBf1'  )
		self.board[(7,2)] = BlackBishop( (7,2), 'bBc8'  )
		self.board[(7,5)] = BlackBishop(  (7,5), 'bBf8' )
		
		self.board[(0,0)] = WhiteRook( (0,0), 'wRa1'  )
		self.board[(0,7)] = WhiteRook( (0,7), 'wRh1' )
		self.board[(7,0)] = BlackRook( (7,0), 'bRa8'  )
		self.board[(7,7)] = BlackRook( (7,7), 'bRh8'  )
		
		self.board[(0,3)] = WhiteQueen( (0,3), 'wQd1'  )
		self.board[(7,3)] = BlackQueen(  (7,3), 'bQd8' )
		
		self.board[(0,4)] = WhiteKing( (0,4), 'wKe1' )
		self.board[(7,4)] = BlackKing( (7,4), 'bKe8' )
					
	
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
		
	
	#return all possible white moves (loop over all pieces, check if white, add all possible moves together, return a list of moves) & check if some moves are illegal
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

		# Check if rook or King move -> not allowed to castle

		if isinstance(self.board[move[0]], WhiteRook) or isinstance(self.board[move[0]], BlackRook) or isinstance(
				self.board[move[0]], WhiteKing) or isinstance(self.board[move[0]], BlackKing):
			self.board[move[0]].can_castle = False
	
		player_color = self.board[move[0]].color
	
		# take care of promotion if there is
		if len(move) == 3 :
			if move[2] == 'Q' :
				if player_color == 'white' :
					self.board[move[0]] = WhiteQueen(move[0], self.board[move[0]].name)
				else :
					self.board[move[0]] = BlackQueen(move[0], self.board[move[0]].name)
					
			if move[2] == 'N' :
				if player_color == 'white' :
					self.board[move[0]] = WhiteKnight(move[0], self.board[move[0]].name)
				else :
					self.board[move[0]] = BlackKnight(move[0], self.board[move[0]].name)
			if move[2] == 'R' :
				if player_color == 'white' :
					self.board[move[0]] = WhiteRook(move[0], self.board[move[0]].name)
				else :
					self.board[move[0]] = BlackRook(move[0], self.board[move[0]].name)
			if move[2] == 'B' :
				if player_color == 'white' :
					self.board[move[0]] = WhiteBishop(move[0], self.board[move[0]].name)
				else :
					self.board[move[0]] = BlackBishop(move[0], self.board[move[0]].name)
					
		# check if "en passant" pawn taken
		
		if len(move) == 4 :
			if move[2] == 'destroy' :
				if player_color == 'white' :
					self.board[tuple(map(operator.add, move[1], (-1,0)) )] = EmptyPiece(tuple(map(operator.add, move[1], (-1,0)) ))
				else :
					self.board[tuple(map(operator.add, move[1], (1,0)) )] = EmptyPiece(tuple(map(operator.add, move[1], (1,0)) ))
		
		# create the virtual pawn for take en passant
		if len(move) == 4 :
			if move[2] == 'create virtual' :
				if player_color == 'white' :
					self.board[tuple(map(operator.add, move[1], (-1,0)) )] = VirtualWhitePawn(tuple(map(operator.add, move[1], (-1,0)) ))
				else :
					self.board[tuple(map(operator.add, move[1], (1,0)) )] = VirtualBlackPawn(tuple(map(operator.add, move[1], (1,0)) ))
		
					
		# Check if Castle O-O or O-O-O (so move 2 pieces, the rook + king) or play the move :
		if 'O-O' in move or 'O-O-O' in move :
			self.board[move[0]].coordinate = move[1]
			self.board[move[1]] = self.board[move[0]]
			self.board[move[0]] = EmptyPiece(move[0])
			self.board[move[2]].coordinate = move[3]
			self.board[move[3]] = self.board[move[2]]
			self.board[move[2]] = EmptyPiece(move[3])

		else:
			self.board[move[0]].coordinate = move[1]
			self.board[move[1]] = self.board[move[0]]
			self.board[move[0]] = EmptyPiece(move[0])
		
		# remove the virtual pawns of the other color
		if player_color == 'white' : 
			for coord in self.board :
				if isinstance(self.board[coord] , VirtualBlackPawn) : self.board[coord] = EmptyPiece(coord)
				
		else : 
			for coord in self.board :
				if isinstance(self.board[coord] , VirtualWhitePawn) : self.board[coord] = EmptyPiece(coord)




		
			
	# translate a move into a pgn string format (like if N in (0,6) : [(0,6), (2, 5) ] -> 'Nf3'). return string. Needs the list of all playable moves to remove ambiguities		
	def move_to_pgn(self, move) :
		
		column_list = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h']
		all_moves_pgn = []
		
		
		pgn_move = ''

		if 'O-O' in move :
			return 'O-O'
		if 'O-O-O' in move :
			return 'O-O-O'
		
		piece_eaten = True
		# if piece_eaten = true -> add a 'x' to the notation
		if isinstance(self.board[move[1]], EmptyPiece) :
			piece_eaten = False
			# separate notation between pawns and the others
		if isinstance(self.board[move[0]], WhitePawn) or isinstance(self.board[move[0]], BlackPawn) :
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
			if isinstance(self.board[move[0]], WhiteKnight) or isinstance(self.board[move[0]], BlackKnight) :
				letter = 'N'
			if isinstance(self.board[move[0]], WhiteBishop) or isinstance(self.board[move[0]], BlackBishop) :
				letter = 'B'
			if isinstance(self.board[move[0]], WhiteRook) or isinstance(self.board[move[0]], BlackRook) :
				letter = 'R'
			if isinstance(self.board[move[0]], WhiteQueen) or isinstance(self.board[move[0]], BlackQueen) :
				letter = 'Q'
			if isinstance(self.board[move[0]], WhiteKing) or isinstance(self.board[move[0]], BlackKing) :
				letter = 'K'
			
		
			if piece_eaten :
				pgn_move = letter + column_list[move[0][1]] + str(move[0][0]+1) + 'x' + column_list[move[1][1]] + str(move[1][0]+1)
			else : 
				pgn_move = letter + column_list[move[0][1]] + str(move[0][0]+1)  + column_list[move[1][1]] + str(move[1][0]+1)
					
			
			

		
					
		return pgn_move
		
		
		
		# Test the king legal moves : Create a copy of the board and test the move. Then check if any of the possible other player move reach the king square. If yes => not legal move and return False. If no, this is a legal move and returns True. This allows to take care of checking moves but also the king cannot suicide.
		# Take also care of checking the castling
	def legal_move(self, player, move) :

		board_projection = copy.deepcopy(self)

		board_projection.play_move(move)
		
		king_position = (-1,-1)

		if player == 'white' :
		
			for square in board_projection.board :
				if isinstance(board_projection.board[square], WhiteKing) :
					king_position = square
					

			if king_position in [x[1] for x in board_projection.black_moves_projection()] :
				return False
			elif 'O-O' in move :
				if (0,5) in [x[1] for x in board_projection.black_moves_projection()] or (0,6) in [x[1] for x in board_projection.black_moves_projection()] :
					return False
				else : return True
			elif 'O-O-O' in move :
				if (0,3) in [x[1] for x in board_projection.black_moves_projection()] or (0,2) in [x[1] for x in board_projection.black_moves_projection()] :
					return False
				else : return True

			else :
				return True

				
				
		if player == 'black' :
			for square in board_projection.board :
				if isinstance(board_projection.board[square], BlackKing) :
					king_position = square
			
			if king_position in [x[1] for x in board_projection.white_moves_projection()] :
				return False
			elif 'O-O' in move :
				if (7,5) in [x[1] for x in board_projection.black_moves_projection()] or (7,6) in [x[1] for x in board_projection.black_moves_projection()] :
					return False
			elif 'O-O-O' in move :
				if (7,3) in [x[1] for x in board_projection.black_moves_projection()] or (7,2) in [x[1] for x in board_projection.black_moves_projection()] :
					return False

			else : 
				return True



	def board2onehot(self, player):

		arr = np.zeros((8,8))

		for key in self.board :
			if isinstance( self.board[key], WhitePawn) : arr[key[0], key[1] ] = 1
			if isinstance( self.board[key], WhiteKnight) : arr[key[0], key[1] ] = 2
			if isinstance(self.board[key], WhiteBishop): arr[key[0] , key[1] ] = 3
			if isinstance(self.board[key], WhiteRook): arr[key[0] , key[1] ] = 4
			if isinstance(self.board[key], WhiteQueen): arr[key[0] , key[1] ] = 5
			if isinstance(self.board[key], WhiteKing): arr[key[0] , key[1] ] = 6
			if isinstance( self.board[key], BlackPawn) : arr[key[0], key[1] ] = 7
			if isinstance( self.board[key], BlackKnight) : arr[key[0], key[1] ] = 8
			if isinstance(self.board[key], BlackBishop): arr[key[0] , key[1] ] = 9
			if isinstance(self.board[key], BlackRook): arr[key[0] , key[1] ] = 10
			if isinstance(self.board[key], BlackQueen): arr[key[0] , key[1] ] = 11
			if isinstance(self.board[key], BlackKing): arr[key[0] , key[1] ] = 12

		hotencoded = Fn.one_hot(torch.tensor(arr).to(torch.int64), -1)
		hotencodedboard1 = hotencoded.permute((2,0,1))
		if player == 'white' :
			hotencodedboard = torch.cat((torch.tensor(np.full((8, 8), 1))[None,:], hotencodedboard1), dim = 0)
		else :
			hotencodedboard = torch.cat((torch.tensor(np.full((8, 8), -1))[None,:], hotencodedboard1), dim = 0)
		return hotencodedboard


	def update_pgn(self, pgn_move):
		"""
		pdate pgn string
		"""
		if self.white_to_play:
			self.pgn_string += f"{str(self.round)}. {pgn_move}"
			self.white_to_play = False
		else:
			self.pgn_string += f" {pgn_move}\n"
			self.round +=1
			self.white_to_play = True

		
	def move2uci(self,move):
		"""
		take a move and return the uci encoding string for this move
		"""

		column_letters = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h']
		actual_letter, next_letter = column_letters[move[0][0]], column_letters[move[1][0]]
		actual_row, next_row = move[1][0] + 1, move[1][1] + 1
		uci_move = f"{actual_letter}{actual_row}{next_letter}{next_row}"

		return uci_move
	
	def coord2string(self, coord: Tuple[int,int]) -> str:
		"""
		take a tuple of coordinates and return string coordinates with letters and row
		"""
		x,y = coord
		column, row = self.columnlist[y], x+1

		return f"{column}{row}"
	
	def string2coord(self, string: str):
		"""
		take column_row string and translate to tuple coordinates
		"""
		column, row = string[0], string[1]
		x, y = int(row) - 1, self.columnlist.index(column)

		return (x,y)

	def readuci(self, ucimove):
		"""
		take an uci move and translate it into chess_board move coordinate
		"""
		
		if ucimove == "e1g1":
			move = [(0,4), (0,6), (0,7), (0,5), 'O-O']
			return move
		elif ucimove == "e1c1":
			move = [(0,4), (0,2), (0,0), (0,3), 'O-O-O']
			return move
		elif ucimove == "e8c8":
			move = [(7,4), (7,2), (7,0), (7,3), 'O-O-O']
			return move
		elif ucimove == "e8g8":
			move = [(7,4), (7,6), (7,7), (7,5), 'O-O']
			return move
		
		if len(ucimove) == 5:
			# differ piece promotion from case moves
			ucimove, promotion_piece = ucimove[:4], ucimove[-1].upper()
			move = self.readuci(ucimove)
			move.append(promotion_piece)
			return move
		
		
		position1, position2 = ucimove[:2], ucimove[2:]
		move = [self.string2coord(position1), self.string2coord(position2)]
		
		return move
	

	def board2fen(self):
    
		game = chess.pgn.read_game(StringIO(self.pgn_string))
		board = game.board()
		for m in game.mainline_moves():
			board.push(m)
			
		return board.fen()

	def neural2chessboardmove(self, neuralmove):
		move = []
		if '=' in neuralmove :
			neurmove = re.split('->|=', neuralmove)
			for square in self.board:
				if self.board[square].name == neurmove[0] :
					move.append(self.board[square].coordinate)
					move.append( (self.linelist.index(neurmove[1][1]) , self.columnlist.index(neurmove[1][0]) ) )
					move.append( neurmove[2] )

		elif 'O-O-O' in neuralmove :
			if 'w' in neuralmove :
				move = [(0, 4), (0, 2), (0, 0), (0, 3), 'O-O-O']
			else :
				move = [(7, 4), (7, 2), (7, 0), (7, 3), 'O-O-O']


		elif 'O-O' in neuralmove :
			if 'w' in neuralmove :
				move = [(0, 4), (0, 6), (0, 7), (0, 5), 'O-O']
			else :
				move = [(7, 4), (7, 6), (7, 7), (7, 5), 'O-O']

		else :
			neurmove = re.split('->', neuralmove)
			for square in self.board:
				if self.board[square].name == neurmove[0]:
					move.append(self.board[square].coordinate)
					move.append((self.linelist.index(neurmove[1][1]), self.columnlist.index(neurmove[1][0])))

		return move
		



		
	
		




 
