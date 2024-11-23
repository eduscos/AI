# Q.2) Write a Python program to implement Depth First Search algorithm. Refer the
# following graph as an Input for the program. [Initial node 2, Goal node=7]
# Ans:-
# graph = {
# '1': ['2', '3','4'],
# '2': ['1', '4', '5'],
# '3': ['1', '4'],
# '4': ['1','2','3'],
# '5': ['2', '6','7,],
# '6': ['5', '7'],
# '7': ['4', '5','6']
# }

# DFS traversal function
def dfs(graph, start, visited):
    if start not in visited:
        print(start, end=' ')
        visited.add(start)
        for neighbor in graph[start]:
        dfs(graph, neighbor, visited)
# Main function to initiate DFS traversal
def main():
    start_node = '2' # You can change the starting node here
    print("Depth-First Search Traversal:")
    visited = set()
    dfs(graph, start_node, visited)

if __name__ == '__main__':
    main()