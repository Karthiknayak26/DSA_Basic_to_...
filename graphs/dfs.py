def dfs(graph,current,visited):
    visited.add(current)
    print(current)
    for neighbour in graph[current]:
        if neighbour not in visited:
            dfs(graph,neighbour,visited)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

visited = set()

dfs(graph, 'A', visited)           
