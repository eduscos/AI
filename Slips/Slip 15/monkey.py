# Q.1)Write a Program to Implement Monkey Banana Problem using Python
# Ans:-

import queue
class State:
    def __init__(self, monkey_row, monkey_col, has_banana):
    self.monkey_row = monkey_row
    self.monkey_col = monkey_col
    self.has_banana = has_banana

def is_valid(state, rows, cols):
    return 0 <= state.monkey_row < rows and 0 <= state.monkey_col < cols

def is_goal(state, banana_row, banana_col):
    return state.monkey_row == banana_row and state.monkey_col == banana_col and
    state.has_banana

def move(state, action):
    new_state = State(state.monkey_row, state.monkey_col, state.has_banana)
    if action == 'UP':
        new_state.monkey_row -= 1
    elif action == 'DOWN':
        new_state.monkey_row += 1
    elif action == 'LEFT':
        new_state.monkey_col -= 1
    elif action == 'RIGHT':
        new_state.monkey_col += 1
    elif action == 'GRAB':
        new_state.has_banana = True
    return new_state

def bfs(start_state, banana_row, banana_col, rows, cols):
    frontier = queue.Queue()
    frontier.put((start_state, []))
    while not frontier.empty():
        current_state, path = frontier.get()
        if is_goal(current_state, banana_row, banana_col):
            return path
        for action in ['UP', 'DOWN', 'LEFT', 'RIGHT', 'GRAB']:
            new_state = move(current_state, action)
        if is_valid(new_state, rows, cols):
            new_path = path + [action]
            frontier.put((new_state, new_path))
    return None

def print_solution(path):
    if path is None:
        print("No solution found.")
    else:
        print("Solution:")
        print(" -> ".join(path))

if __name__ == "__main__":
    rows = 4
    cols = 4
    monkey_start = (3, 0)
    banana_location = (0, 3)
    start_state = State(monkey_start[0], monkey_start[1], False)
    solution_path = bfs(start_state, banana_location[0], banana_location[1], rows, cols)
    print_solution(solution_path)
    