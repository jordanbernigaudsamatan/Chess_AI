from Class_board import ChessBoard
from PlayersClass import PlayerDQN, PlayerStockfish
import numpy as np


weights_path = ""

prob = np.random()
if prob > 0.5:
    whitePlayer = PlayerDQN(color="white")
    BlackPlayer = PlayerStockfish(color="black")
else:
    whitePlayer = PlayerStockfish(color="white")
    BlackPlayer = PlayerDQN(color="black")


chessboard = ChessBoard()
replaymemory = []
end = False
while not end:
    replaymemory.append(chessboard.board2fen())
    if "endgame":
        end = True
        winner, _, _ = chessboard.engame()
        break

    board_tensor = chessboard.board2onehot()
    move = whitePlayer.boardmove(chessboard)
    chessboard.play_move(move)

    if "endgame":
        end = True
        winner, _, _ = chessboard.engame()
        break

    replaymemory.append(chessboard.board2fen())
    board_tensor = chessboard.board2onehot()
    move = BlackPlayer.boardmove(chessboard)
    chessboard.play_move(move)
