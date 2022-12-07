import torch
import random as rd
from Class_board import ChessBoard

class ReplayMemory():
    """
    """

    def __init__(self, white_agent, black_agent, nb_games, nb_transitions, endgame_transitions=0):
        """
        """

        self.white = white_agent
        self.black = black_agent
        self.nb_games = nb_games
        self.nb_transitions = nb_transitions
        self.endgame_transitions = endgame_transitions
        self.neural_inputs = []


# 2 ways of defining target network:
#   - Opponent next move
#   - Self + 2 moves

    def game(self):
        # output: (state1, state2) if not end
        # or (state1, endgame) if end
        chessboard = ChessBoard()
        chessboard.initialize()

        for i in range(300):

            if chessboard.end:
                break
            # white move
            transition_white1 = chessboard.board2onehot()[None,:]
            white_moves = chessboard.white_moves()
            move = rd.choice(white_moves)
            chessboard.play_move(move)
            print(chessboard.fiftymoverule)
            transition_black2 = chessboard.board2onehot()[None,:]
            transition_black = torch.stack((transition_black1,transition_black2), dim=0)
            endgame = chessboard.endgame()
            self.neural_inputs.append((transition_black, endgame))
            

            if chessboard.end:
                break

            # black move
            transition_black1 = chessboard.board2onehot()[None,:]
            black_moves = chessboard.black_moves()
            move = rd.choice(black_moves)
            chessboard.play_move(move)
            transition_white2 = chessboard.board2onehot()[None,:]

            # stack transition white
            endgame = chessboard.endgame()
            transition_white = (transition_white1, endgame) if chessboard.end else torch.stack((transition_white1,transition_white2), dim=0)
            self.neural_inputs.append((transition_white, endgame))

