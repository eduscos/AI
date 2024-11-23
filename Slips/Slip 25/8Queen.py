# Q.2) Write a Python program to simulate 8-Queens problem.
# Ans:-

def print_chessboard(chessboard):
    for row in chessboard:
        print(" ".join(row))

# Function to check if it's safe to place a queen at the given position
def is_safe(chessboard, row, col, n):
    # Check row on the left side
    for i in range(col):
        if chessboard[row][i] == 'Q':
            return False

# Check upper diagonal on the left side
for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
    if chessboard[i][j] == 'Q':
        return False

# Check lower diagonal on the left side
for i, j in zip(range(row, n, 1), range(col, -1, -1)):
    if chessboard[i][j] == 'Q':
        return False
    return True

# Recursive function to solve the Eight Queens problem
def solve_eight_queens(chessboard, col, n):
    if col >= n:
        return True # All queens are placed
    for i in range(n):
        if is_safe(chessboard, i, col, n):
            chessboard[i][col] = 'Q' # Place a queen
    # Recur to place the rest of the queens
    if solve_eight_queens(chessboard, col + 1, n):
        return True
    # If placing a queen doesn't lead to a solution, backtrack
    chessboard[i][col] = '.'
    return False # No solution exists

# Main function to solve the Eight Queens problem
def main():
    n = 8 # Size of the chessboard (8x8)
    chessboard = [['.' for _ in range(n)] for _ in range(n)]

    if solve_eight_queens(chessboard, 0, n):
        print("Solution to the Eight Queens Problem:")
        print_chessboard(chessboard)
    else:
        print("No solution found.")

if __name__ == '__main__':
    main()