def dls(graph, node, depth, visited):
    if depth < 0:
        return

    print(node, end=" ")

    if depth == 0:
        return

    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dls(graph, neighbor, depth - 1, visited)

def iddfs(graph, start, max_depth):
    for depth in range(max_depth + 1):
        print("\nDepth", depth, ":")
        dls(graph, start, depth, set())

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

iddfs(graph, 'A', 3)
