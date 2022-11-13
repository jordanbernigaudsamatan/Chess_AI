from dqn_architecture import ChessDQn
import torch
from pathlib import Path
import json
from stockfish import Stockfish
from Class_board import ChessBoard

class PlayerDQN:

    def __init__(self, color, epsilon=0.5, weights=None):
        self.model = ChessDQn()
        if weights:
            self.model.load_state_dict(weights)
        self.color = color
        self.epsilon = epsilon
        self.neuraldict_reverse = json.load(Path("NeuralDict.json").open())
        self.neuraldict_reverse = {v: k for (k, v) in self.neuraldict_reverse.items()}

    def predict(self, chessboard: ChessBoard) -> torch.Tensor:
        input = chessboard.board2onehot()
        return self.model(input)

    def choose_move(self, q_values: torch.Tensor):

        q_val_index = torch.argmax(q_values) + 1
        q_val = torch.max(q_values)
        return self.neuraldict[q_val_index], q_val
    
    def boardmove(self, chessboard: ChessBoard):
        q_values = self.predict(chessboard)
        neuralmove = self.choose_move(q_values)
        chessboard_move = chessboard.neural2boardmove(neuralmove) # new fonction to write by jordan
        return chessboard_move


class PlayerStockfish():

    def __init__(self, path, color, elo=50):

        self.stockfish_model = Stockfish(path=path)
        self.stockfish_model.set_elo_rating(elo)
        self.color = color

    def boardmove(self, chessboard: ChessBoard):
        
        fen = chessboard.pgn2fen()
        self.stockfish_model.set_fen_position(fen)
        uci_move = self.stockfish_model.get_best_move()
        chessboard_move = chessboard.readuci(ucimove=uci_move)
        return chessboard_move