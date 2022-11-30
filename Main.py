import numpy as np
from Class_Pieces import *
from Class_board import *
import random
from matplotlib.backends.backend_pdf import PdfPages
import os


# =================================== Create a chess board class and set up the begining game ===============================

chessboard = ChessBoard()

chessboard.initialize()
#print(chessboard.board2onehot('white'))


move = chessboard.neural2chessboardmove("bBf8->b8")
print(move)
print(move[0])
print('A')
chessboard.play_move(move)
chessboard.human_visualize()
'''
pgn = ''
for i in range(5):

    if chessboard.white_moves() == []: break

    white_move = random.choice(chessboard.white_moves())
    print('White Play : ', chessboard.move_to_pgn(white_move))
    pgn += str(i + 1) + '. ' + chessboard.move_to_pgn(white_move)
    chessboard.play_move(white_move)

    if chessboard.black_moves() == []: break

    black_move = random.choice(chessboard.black_moves())
    print('Black Play : ', chessboard.move_to_pgn(black_move))
    pgn += ' ' + chessboard.move_to_pgn(black_move) + '\n'
    chessboard.play_move(black_move)

print(pgn)
chessboard.human_visualize()



#chessboard.human_visualize()
'''


'''
pgn = ''

pgn += '1. '+chessboard.move_to_pgn([(1,4), (2,4)])
pgn += ' '+chessboard.move_to_pgn([(6,4), (5,4)])+'\n'
pgn += '2. '+chessboard.move_to_pgn([(0,5), (2,3)] )
pgn += ' '+chessboard.move_to_pgn([(7,5), (5,3)])+'\n'
pgn += '3. '+chessboard.move_to_pgn([(0,6), (2,7)])
pgn += ' '+chessboard.move_to_pgn([(7,6), (5,7)])+'\n'
os.system('rm multipage_pdf.pdf')


chessboard.play_move( [(1,4), (2,4)] )
chessboard.play_move( [(6,4), (5,4)] )
chessboard.play_move( [(0,5), (2,3)] )
chessboard.play_move( [(7,5), (5,3)] )
chessboard.play_move( [(0,6), (1,7)] )
chessboard.play_move( [(7,6), (5,7)] )

print(chessboard.white_moves())
with PdfPages('multipage_pdf.pdf') as pdf:
	for i in range(1,30) :
	
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


'''

'''
#Test castle

chessboard.play_move([(0,6), (2, 7)])
chessboard.play_move([(7,6), (2, 4)])
chessboard.play_move([(0,5), (3, 2)])
chessboard.play_move([(0,6), (2, 7)])
chessboard.human_visualize()
print(chessboard.white_moves())

'''

#Test taken en passant

'''
chessboard.play_move([(1,0), (3, 0), 'create virtual', 'white'])
chessboard.play_move([(6,5), (5, 5)])
chessboard.play_move([(3,0), (4, 0)])
chessboard.play_move([(6,1), (4, 1), 'create virtual', 'black'])
chessboard.play_move([(4, 0), (5, 0)])
chessboard.human_visualize()
print(chessboard.white_moves())
'''













 
