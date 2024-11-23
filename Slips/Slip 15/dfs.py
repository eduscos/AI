# Q.2) Write a program to implement Iterative Deepening DFS algorithm.
# [Goal Node=G]
# Ans:-

class Node:
    def __init__(self, state, children=None):
    self.state = state
    self.children = children if children else []

def depth_limited_dfs(node, goal_state, depth_limit, current_depth=0):
    if current_depth > depth_limit:
        return None
    if node.state == goal_state:
        return [node.state]
    for child in node.children:
        path = depth_limited_dfs(child, goal_state, depth_limit, current_depth + 1)
    if path is not None:
        return [node.state] + path
        return None

def iterative_deepening_dfs(root, goal_state):
    depth_limit = 0
    while True:
        result = depth_limited_dfs(root, goal_state, depth_limit)
    if result is not None:
        return result
    depth_limit += 1

if __name__ == "__main__":
    # Example usage:
    # Creating a simple tree structure for demonstration
    root = Node("A", [Node("B", [Node("D", [Node("G")])]), Node("C", [Node("E"),
    Node("F", [Node("H", [Node("I")])])])])
    goal_node = "G"
    solution_path = iterative_deepening_dfs(root, goal_node)
    if solution_path:
        print("Solution Path:", " -> ".join(solution_path))
    else:
        print("No solution found.")