import stockfish
import chess
import chess.pgn
from Class_board import ChessBoard
from io import StringIO
from typing import AnyStr


def pgn2fen(pgn_string: AnyStr) -> AnyStr:
    """
    take a pgn string and return a fen string
    """
    game = chess.pgn.read_game(StringIO(pgn_string))
    board = game.board()
    for m in game.mainline_moves():
        board.push(m)
    return board.fen()