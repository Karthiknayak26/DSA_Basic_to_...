from collections import deque
def bfs(graph,start):
    visited=set()
    queue=deque()
    visited.add(start)
    queue.append(start)
    while queue:
        current=queue.popleft()
        print(current)
        for neighbour in graph[current]:
            if neighbour not in  visited:
                visited.add(neighbour)
                queue.append(neighbour)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

bfs(graph, 'A')