from AILogic import board
import numpy as np

def encode_board(board):
    board_state = board.current_board
    encoded = np.zeros([10,6,7]).astype(int)
    encoder_dict = {"O":0, "X":1}
    for row in range(6):
        for col in range(7):
            if board_state[row,col] != " ":
                encoded[row, col, encoder_dict[board_state[row,col]]] = 1
    if board.player == 1:
        encoded[:,:,2] = 1 # player to move
    return encoded
