# Q.1) Write a Program to Implement Alpha-Beta Pruning using Python
# Ans:-

import math

def alpha_beta_pruning(board, depth, alpha, beta, is_maximizing_player):
    if depth == 0 or game_over(board):
        return evaluate(board)
    if is_maximizing_player:
        max_eval = -math.inf
        for move in possible_moves(board):
        board[move] = 'X'
        eval = alpha_beta_pruning(board, depth - 1, alpha, beta, False)
        board[move] = ' ' # undo the move
        max_eval = max(max_eval, eval)
        alpha = max(alpha, eval)
        if beta <= alpha:
            break # Beta cut-off
            return max_eval
        else:
            min_eval = math.inf
        for move in possible_moves(board):
            board[move] = 'O'
            eval = alpha_beta_pruning(board, depth - 1, alpha, beta, True)
            board[move] = ' ' # undo the move
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
        
        if beta <= alpha:
            break # Alpha cut-off
            return min_eval

def game_over(board):
    # Implement your game-over condition (e.g., check for a winner or a draw)
    return False

def evaluate(board):
    # Implement your evaluation function based on the current state of the board
    return 0

def possible_moves(board):
    # Implement generating a list of possible moves based on the current state of the
    board
    return []

if __name__ == "__main__":
    # Example usage:
    initial_board = [' '] * 9 # Assume a Tic-Tac-Toe board for simplicity
    depth_limit = 3
    best_move = -1
    best_value = -math.inf

for move in possible_moves(initial_board):
    initial_board[move] = 'X'
    move_value = alpha_beta_pruning(initial_board, depth_limit - 1, -math.inf, math.inf,False)
    initial_board[move] = ' ' # undo the move
    if move_value > best_value:
        best_value = move_value
        best_move = move

print(f"The best move is {best_move} with a value of {best_value}")