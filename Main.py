import numpy as np
from Class_Pieces import *
from Class_board import *
import random
from matplotlib.backends.backend_pdf import PdfPages
import os


# =================================== Create a chess board class and set up the begining game ===============================

chessboard = chess_board()

chessboard.initialize()

chessboard.human_visualize()

pgn = ''

os.system('rm multipage_pdf.pdf')
with PdfPages('multipage_pdf.pdf') as pdf:
	for i in range(110) :
	
		if chessboard.white_moves() == [] : break

	
		white_move = random.choice(chessboard.white_moves())
		print('White Play : ', chessboard.move_to_pgn(white_move))
		pgn += str(i+1)+'. '+chessboard.move_to_pgn(white_move)
		chessboard.play_move(white_move)
	
		
		if chessboard.black_moves() == [] : break

		black_move = random.choice(chessboard.black_moves())
		print('Black Play : ', chessboard.move_to_pgn(black_move))
		pgn += ' '+chessboard.move_to_pgn(black_move)+'\n'
		chessboard.play_move(black_move)
		
		

		#chessboard.human_visualize()

		

print(pgn)


 
