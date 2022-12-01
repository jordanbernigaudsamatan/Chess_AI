from Class_board import ChessBoard
import random as rd
from tqdm import tqdm
# =================================== Create a chess board class and set up the begining game ===============================

# Initialize chessboard
chessboard = ChessBoard()
chessboard.initialize()
i=0

for i in tqdm(range(500)):

	endgame = chessboard.endgame()
	if chessboard.end:
		print(endgame)
		break
	# white move
	white_moves = chessboard.white_moves()
	move = rd.choice(white_moves)
	chessboard.play_move(move)
	
	endgame = chessboard.endgame()
	if chessboard.end:
		print(endgame)
		break
	# black move
	black_moves = chessboard.black_moves()
	move = rd.choice(black_moves)
	chessboard.play_move(move)


pgn = chessboard.pgn_string
print(pgn)