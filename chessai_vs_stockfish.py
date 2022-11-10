from Class_board import chess_board
from stockfish_utils import pgn2fen
from stockfish import Stockfish
import random as rd


chessboard = chess_board()
chessboard.initialize()
stockfish_engine = Stockfish(str('/home/jordan/Bureau/stockfish_15_linux_x64/stockfish-15-64'))
chessboard.readuci("e8c8")
chessboard.readuci("g7h8q")
end = False
while not end:

    if chessboard.white_moves() == []:
        end = True
        continue

    white_move = rd.choice(chessboard.white_moves())
    chessboard.update_pgn(chessboard.move_to_pgn(white_move))
    chessboard.play_move(white_move)

    if chessboard.black_moves() == []:
        end = True

    fen = pgn2fen(chessboard.pgn_string)
    stockfish_engine.set_fen_position(fen)

    black_move = stockfish_engine.get_best_move()
    black_move = chessboard.readuci(black_move)
    chessboard.update_pgn(chessboard.move_to_pgn(black_move))
    chessboard.play_move(black_move)

print(chessboard.pgn_string)