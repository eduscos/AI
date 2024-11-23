# Q.1) Write python program to solve 8 puzzle problem using A algorithm [10
# marks]
# Ans:-

import heapq
class PuzzleNode:
    
    def __init__(self, state, parent=None, move=None, cost=0, heuristic=0):
        self.state, self.parent, self.move, self.cost, self.heuristic = state, parent, move, cost, heuristic
    
    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def manhattan_distance(state):
        return sum(abs((val-1)%3 - i%3) + abs((val-1)//3 - i//3) for i, val in enumerate(state) if val)
    
    def neighbors(node):
        zero_i = node.state.index(0)
        moves = [1, -1, 3, -3]
        return [PuzzleNode(list(node.state[:zero_i] + [node.state[zero_i + m]] +

node.state[zero_i + m + 1:]), node, m, node.cost + 1, manhattan_distance(node.state))
for m in moves if 0 <= zero_i + m < 9 and (m == 1 or m == -1 or m == 3 or m == -3)]

def print_solution(node):
    moves = []
    while node.parent:
        moves.append("Move right" if node.move == 1 else "Move left" if node.move == -1
        else "Move down" if node.move == 3 else "Move up")
        node = node.parent
    moves.reverse()
    print("Solution found!\n" + '\n'.join(moves))
        
def solve_puzzle(initial_state):
    goal, frontier, explored = [1, 2, 3, 4, 5, 6, 7, 8, 0], [PuzzleNode(initial_state, None, None, 0, manhattan_distance(initial_state))], set()
    while frontier:
        current_node = heapq.heappop(frontier)
        if current_node.state == goal:
            print_solution(current_node)
            return
        explored.add(tuple(current_node.state))
        
        for neighbor in [n for n in neighbors(current_node) if tuple(n.state) not in explored]:
            heapq.heappush(frontier, neighbor)
        print("No solution found.")

if __name__ == "__main__":
    solve_puzzle([1, 2, 3, 4, 5, 6, 0, 7, 8]) # Replace with your initial state