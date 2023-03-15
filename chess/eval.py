import chess
import chess.svg
import chess.engine
import time
import random
import numpy as np

#file letter to index
squares_index = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7
}

#return board index from square
def square_to_index(square):
    letter = chess.square_name(square)
    return 8-int(letter[1]), squares_index[letter[0]]

#transform board to numpy representation
def board_to_numpy(board):
    board3d = np.zeros((14,8,8), dtype=np.int8)

    for piece in chess.PIECE_TYPES:
        for square in board.pieces(piece, chess.WHITE):
            idx = np.unravel_index(square, (8,8))
            board3d[piece - 1][7 - idx[0]][idx[1]] = 1
        for square in board.pieces(piece, chess.BLACK):
            idx = np.unravel_index(square, (8,8))
            board3d[piece + 5][7 - idx[0]][idx[1]] = 1
    
    temp = board.turn
    board.turn = chess.WHITE
    for move in board.legal_moves:
        i,j = square_to_index(move.to_square)
        board3d[12][i][j] = 1
    board.turn = chess.BLACK
    for move in board.legal_moves:
        i,j = square_to_index(move.to_square)
        board3d[13][i][j] = 1

    board.turn = temp

    return board3d

#create "random" board state by making random number of moves (between 0,200)
def random_board(max_depth=200):
    board = chess.Board()
    depth = random.randrange(0, max_depth)

    for i in range(depth):
        all_moves = list(board.legal_moves)
        random_move = random.choice(all_moves)
        board.push(random_move)
        if board.is_game_over():
            break
    return board

#return stockfish evaluation of position
def stockfish_evaluation(board, depth_=10):
    engine = chess.engine.SimpleEngine.popen_uci("stockfish_15.1_win_x64_avx2\stockfish-windows-2022-x86-64-avx2.exe")
    result = engine.analyse(board, chess.engine.Limit(depth=depth_))
    if result["score"].is_mate():
        print("mate")
        return result["score"].white().mate()
    print(board.fen)
    print(result["score"].white().score())
    return result["score"].white().score()

def add_data():
    board = random_board()
    with open("positions.npy", "ab") as f:
        np.save(f, np.array([board_to_numpy(board)]))
    f.close()
    with open("eval.npy", "ab") as f:
        np.save(f, np.array([stockfish_evaluation(board,25)/100]))   
    f.close()

def get_data(n):
    with open("positions.npy", "rb") as f:
        for i in range(n):
            #positions = np.array([])
            positions = np.load(f,allow_pickle=True)
    f.close()
    with open("eval.npy", "rb") as f:
        eval = np.load(f,allow_pickle=True)
    f.close()
    for i in range(len(positions)):
        print(positions[i])
        print(f"eval: {eval[i]}")
        
#board = chess.Board("rbp2b2/4Q3/2q5/1kR2r2/3B2q1/4nrn1/2r1N3/2K3N1 w - - 0 1")
"""
board = random_board()
print(board)
print(board.fen)
print(board_to_numpy(board))

result = stockfish_evaluation(board,25)
print(result/100)
"""
def main(num_positions):
    for i in range(num_positions):
        add_data()
    for i in range(num_positions):
        get_data()

main(5)