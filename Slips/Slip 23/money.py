# Q.2) Write a Python program for the following Cryptarithmetic problems SEND +
# MORE = MONEY
# Ans:-

from itertools import permutations

def is_solution(mapping):
    send = mapping['S'] * 1000 + mapping['E'] * 100 + mapping['N'] * 10 + mapping['D']
    more = mapping['M'] * 1000 + mapping['O'] * 100 + mapping['R'] * 10 + mapping['E']
    money = mapping['M'] * 10000 + mapping['O'] * 1000 + mapping['N'] * 100 +
    mapping['E'] * 10 + mapping['Y']
    return send + more == money

def solve_cryptarithmetic():
    for p in permutations(range(10), 8):
        mapping = {'S': p[0], 'E': p[1], 'N': p[2], 'D': p[3], 'M': p[4], 'O': p[5], 'R': p[6], 'Y': p[7]}
        if is_solution(mapping):
            return mapping
    return None

if __name__ == "__main__":
    solution = solve_cryptarithmetic()
    if solution:
        print("Solution found:")
        print(f" S = {solution['S']}")
        print(f" E = {solution['E']}")
        print(f" N = {solution['N']}")
        print(f" D = {solution['D']}")
        print(f" M = {solution['M']}")
        print(f" O = {solution['O']}")
        print(f" R = {solution['R']}")
        print(f" Y = {solution['Y']}")
        print("\n SEND")
        print("+ MORE")
        print("------")
        print(f" MONEY")
    else:
        print("No solution found.")
        