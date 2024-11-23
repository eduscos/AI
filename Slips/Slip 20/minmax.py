# Q.1 Write a Python program to implement Mini-Max Algorithm.
# Ans:-
import math

def evaluate(board):
    return sum(row.count('X') - row.count('O') for row in board)

def is_terminal(board):
    return any(' ' not in row for row in board) or evaluate(board) != 0

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def mini_max(board, depth, maximizing_player):
    if is_terminal(board):
        return evaluate(board)
    return max(mini_max(make_move(board, move, 'X'), depth + 1, False) if maximizing_player else mini_max(make_move(board, move, 'O'), depth + 1, True) for move in get_available_moves(board))

def find_best_move(board):
    return max(get_available_moves(board), key=lambda move:
        mini_max(make_move(board, move, 'X'), 0, False))

def make_move(board, move, player):
    i, j = move
    new_board = [row.copy() for row in board]
    new_board[i][j] = player
    return new_board

def print_board(board):
    for row in board:
        print(" ".join(cell for cell in row))
        print()

def play_game():

    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Initial Board:")
    print_board(board)

    for _ in range(4): # Play four moves for demonstration
        player_move = tuple(map(int, input("Enter your move (row and column separated by space): ").split()))
        board = make_move(board, player_move, 'O')
        print("Updated Board after your move:")
        print_board(board)
 
        if is_terminal(board):
            print("Game over!")
            break

        print("Computer's move:")

        computer_move = find_best_move(board)
        board = make_move(board, computer_move, 'X')
        
        print("Updated Board after computer's move:")
        print_board(board)
        
        if is_terminal(board):
            print("Game over!")
            break

if __name__ == "__main__":
play_game()