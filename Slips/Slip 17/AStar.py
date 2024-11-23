# Q.2) Write a Python program to implement A* algorithm. Refer the following graph
# as an Input for the program. Start vertex is A and Goal Vertex is G]
# Ans:-

import heapq

# Graph represented as an adjacency list
graph = {
'A': {'B': 9, 'C': 4, 'D':7},
'B': {'A': 9, 'E': 11},
'C': {'A': 4, 'E': 17, 'F': 12},
'D': {'A': 7, 'F': 14},
'E': {'B': 11, 'C': 17, 'G': 5},
'F': {'C': 12, 'D': 14,'G': 9},
'G': {'E': 5, 'F': 9}
}

# Heuristic function (replace with your own heuristic)
heuristic = {
'A': 21,
'B': 14,
'C': 18,
'D': 18,
'E': 5,
'F': 8,
'G': 0
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
    goal_vertex = 'G'
    result_cost = astar(start_vertex, goal_vertex)
    if result_cost != float('inf'):
        print(f"Cost from {start_vertex} to {goal_vertex} using A* algorithm: {result_cost}")
    else:
        print(f"No path found from {start_vertex} to {goal_vertex}.")