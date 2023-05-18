import chess
import chess.engine
import random

#return a python-chess board from a fen string
def fen_to_board(fen):
    board = chess.Board(fen)
    return board

#find best move according to stockfish
def best_move(board,depth_=10):
    engine = chess.engine.SimpleEngine.popen_uci("stockfish\stockfish_15.1_win_x64_avx2\stockfish-windows-2022-x86-64-avx2.exe")
    result = engine.play(board, chess.engine.Limit(depth=depth_))
    return result

#find stockfish evaluation
def stockfish_evaluation(board, depth_=10):
        engine = chess.engine.SimpleEngine.popen_uci("stockfish\stockfish_15.1_win_x64_avx2\stockfish-windows-2022-x86-64-avx2.exe")
        result = engine.analyse(board, chess.engine.Limit(depth=depth_))
        if result["score"].is_mate():
            print(result["score"].white().mate())
            return result["score"].white().mate()
        return result["score"].white().score()/100

#generate random board as a python-chess library board
def random_board(max_depth=200):
        board = chess.Board()
        depth = random.randrange(1, max_depth)

        for i in range(depth):
            all_moves = list(board.legal_moves)
            random_move = random.choice(all_moves)
            board.push(random_move)
            if board.is_game_over():
                break
        return board

#return best move, takes fen string and depth for stockfish
def best_move_from_fen(fen,depth):
    board = fen_to_board(fen)
    return best_move(board,depth)