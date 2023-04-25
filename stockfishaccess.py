import chess
import chess.engine
import random


def best_move(board,_depth=10):
    engine = chess.engine.SimpleEngine.popen_uci("stockfish\stockfish_15.1_win_x64_avx2\stockfish-windows-2022-x86-64-avx2.exe")
    result = engine.play(board, chess.engine.Limit(depth=_depth))
    print(board.fen)
    return result

def stockfish_evaluation(board, depth_=10):
        engine = chess.engine.SimpleEngine.popen_uci("stockfish\stockfish_15.1_win_x64_avx2\stockfish-windows-2022-x86-64-avx2.exe")
        result = engine.analyse(board, chess.engine.Limit(depth=depth_))
        if result["score"].is_mate():
            print("mate")
            print(result["score"].white().mate())
            return result["score"].white().mate()
        print(board.fen)
        print(result["score"].white().score())
        return result["score"].white().score()/100

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
