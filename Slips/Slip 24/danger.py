# Q.2) Write a Python program for the following Crypt arithmetic problems
# CROSS+ROADS = DANGER
# Ans:-

from itertools import permutations

def is_solution(mapping):
    cross = mapping['C'] * 10000 + mapping['R'] * 1000 + mapping['O'] * 100 +
    mapping['S'] * 10 + mapping['S']
    roads = mapping['R'] * 10000 + mapping['O'] * 1000 + mapping['A'] * 100 +
    mapping['D'] * 10 + mapping['S']
    danger = mapping['D'] * 100000 + mapping['A'] * 10000 + mapping['N'] * 1000 +
    mapping['G'] * 100 + mapping['E'] * 10 + mapping['R']
    return cross + roads == danger

def solve_cryptarithmetic():
    for p in permutations(range(10), 8):
    mapping = {'C': p[0], 'R': p[1], 'O': p[2], 'S': p[3], 'A': p[4], 'D': p[5], 'N': p[6], 'G': p[7],
    'E': p[8]}
    if is_solution(mapping):
        return mapping
    return None

if __name__ == "__main__":
    solution = solve_cryptarithmetic()
    if solution:
        print("Solution found:")
        print(f" C = {solution['C']}")
        print(f" R = {solution['R']}")
        print(f" O = {solution['O']}")
        print(f" S = {solution['S']}")
        print(f" A = {solution['A']}")
        print(f" D = {solution['D']}")
        print(f" N = {solution['N']}")
        print(f" G = {solution['G']}")
        print(f" E = {solution['E']}")
        print("\n CROSS")
        print("+ ROADS")
        print("------")
        print(f" DANGER")
    else:
        print("No solution found.")
        