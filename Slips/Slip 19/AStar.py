# Q.2) Write a Python program to implement A* algorithm. Refer the following graph
# as an Input for the program.
# Ans:-

import heapq
# Graph represented as an adjacency list
graph = {
'A': {'B': 2, 'E': 3},
'B': {'A': 2, 'C': 1,'F':9},
'C': {'B': 1},
'D': {'E': 6, 'F': 1},
'E': {'A': 3, 'D': 6},
'F': {'B': 9, 'D': 1},
}
# Heuristic function (replace with your own heuristic)
heuristic = {
'A': 11,
'B': 6,
'C': 99,
'D': 1,
'E': 7,
'F': 0,
}
def astar(start, goal):
    priority_queue = [(0, start)]
    visited = set()
    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)
        if current_node == goal:
        return current_cost
        if current_node not in visited:
        visited.add(current_node)
        for neighbor, edge_cost in graph[current_node].items():
        heuristic_cost = heuristic[neighbor]
        total_cost = current_cost + edge_cost + heuristic_cost
        heapq.heappush(priority_queue, (total_cost, neighbor))
    return float('inf') # No path found

if __name__ == "__main__":
    start_vertex = 'A'
    goal_vertex = 'F'
    result_cost = astar(start_vertex, goal_vertex)

if result_cost != float('inf'):
    print(f"Cost from {start_vertex} to {goal_vertex} using A* algorithm: {result_cost}")
else:
    print(f"No path found from {start_vertex} to {goal_vertex}.")