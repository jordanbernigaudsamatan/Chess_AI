from Class_board import ChessBoard
import random as rd
# =================================== Create a chess board class and set up the begining game ===============================

# Initialize chessboard
chessboard = ChessBoard()
chessboard.initialize()
i=0

for i in range(300):

	endgame = chessboard.endgame()
	if chessboard.end:
		print(endgame)
		break
	# white move
	white_moves = chessboard.white_moves()
	move = rd.choice(white_moves)
	chessboard.play_move(move)
	print(chessboard.fiftymoverule)
	
	endgame = chessboard.endgame()
	if chessboard.end:
		print(endgame)
		break
	# black move
	black_moves = chessboard.black_moves()
	move = rd.choice(black_moves)
	chessboard.play_move(move)
	print(chessboard.fiftymoverule)


print(chessboard.pgn_string)
print(chessboard.pgn2fen())
chessboard.fen2pgn("r3k2r/pq2bpp1/np1p1n2/2pp3p/3B3P/4PB2/1RPPKP1R/3Q2N1 w k - 5 21")