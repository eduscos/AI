# Q.2) Write a Python program to implement Breadth First Search algorithm. Refer
# the following graph as an Input for the program. [Initial node=1,Goal node=8]
# Ans:
# from collections import deque
# # Define an example graph as an adjacency list
# graph = {
# '1': ['2', '4'],
# '2': ['3'],
# '3': ['5', '6'],
# '4': ['2'],
# '5': ['7', '8'],
# '6': ['8'],
# '7': ['8']
# }

# BFS traversal function
def bfs(graph, start):
    visited = set() # To keep track of visited nodes
    queue = deque() # Create a queue for BFS
    visited.add(start)
    queue.append(start)
    while queue:
        node = queue.popleft()
        print(node, end=' ')

for neighbor in graph[node]:
    if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)

# Main function to initiate BFS traversal
def main():
    start_node = '1' # You can change the starting node here
    print("Breadth-First Search Traversal:")
    bfs(graph, start_node)

if __name__ == '__main__':
main()