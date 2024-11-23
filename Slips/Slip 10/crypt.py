# Q.1) Write Python program to implement crypt arithmetic problem TWO +
# TWO=FOUR
# Ans:-

from itertools import permutations

def is_valid_assignment(mapping, word):
    return int(''.join(mapping[ch] for ch in word))

def solve_cryptarithmetic_puzzle():
    puzzle = ["TWO", "TWO", "FOUR"]
    unique_chars = set(''.join(puzzle))
    
    if len(unique_chars) > 10:
        print("Invalid puzzle: More than 10 unique characters.")
        return
    
    for perm in permutations("0123456789", len(unique_chars)):
        mapping = dict(zip(unique_chars, perm))
        if mapping[puzzle[0][0]] != '0' and is_valid_assignment(mapping, puzzle[0]) + is_valid_assignment(mapping, puzzle[1]) == is_valid_assignment(mapping, puzzle[2]):
        print("Solution found:")
        for word in puzzle:
            print(f"{word}: {is_valid_assignment(mapping, word)}")
        return

    print("No solution found.")

if __name__ == "__main__":
    solve_cryptarithmetic_puzzle()