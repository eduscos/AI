# Q.2) Write a Python program for the following Cryptarithmetic problems. GO + TO
# = OUT
# Ans:-

from itertools import permutations

def is_solution(mapping):
    go = mapping['G'] * 10 + mapping['O']
    to = mapping['T'] * 10 + mapping['O']
    out = mapping['O'] * 100 + mapping['U'] * 10 + mapping['T']
    return go + to == out

def solve_cryptarithmetic():
    for p in permutations(range(10), 5):
        mapping = {'G': p[0], 'O': p[1], 'T': p[2], 'U': p[3], 'N': p[4]}
       if is_solution(mapping):
            return mapping
    return None

if __name__ == "__main__":
    solution = solve_cryptarithmetic()
if solution:
    print("Solution found:")
    print(f" G = {solution['G']}")
    print(f" O = {solution['O']}")
    print(f" T = {solution['T']}")
    print(f" U = {solution['U']}")
    print(f" N = {solution['N']}")
    print("\n GO")
    print("+ TO")
    print("------")
    print(f" OUT")
else:
    print("No solution found.")