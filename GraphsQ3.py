import sys
from queue import PriorityQueue

class Tuple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __lt__(self, other):
        return self.x < other.x

def read_directed_graph():
    n, m = map(int, input().split())
    adjacency = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adjacency[u].append(Tuple(v, w))
    return adjacency

def dijkstras(graph, s):
    dist = [float('inf')] * len(graph)
    pq = PriorityQueue()
    dist[s] = 0
    pq.put(Tuple(0, s))

    while not pq.empty():
        top = pq.get()
        d, u = top.x, top.y
        if d > dist[u]:
            continue
        for edge in graph[u]:
            v, w = edge.x, edge.y
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pq.put(Tuple(dist[v], v))
    return dist

def bellman_ford(graph, start):
    dist = [float('inf')] * len(graph)
    dist[start] = 0

    for _ in range(len(graph) - 1):
        for u in range(len(graph)):
            for edge in graph[u]:
                v, w = edge.x, edge.y
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    return dist

def shortest_paths(graph):
    V = len(graph)
    # Clone the graph to preserve the original structure without the additional vertex
    new_graph = [list(edges) for edges in graph]
    # Append an empty list for the new vertex q
    graph.append([])
    q = V  # New vertex index
    # Add edges from the new vertex q to all other vertices with weight 0
    for i in range(V):
        graph[q].append(Tuple(i, 0))

    initial_dist = bellman_ford(graph, q)

    # Adjust weights in the original graph based on distances calculated from the new vertex q
    for u in range(V):
        for j in range(len(new_graph[u])):
            edge = new_graph[u][j]
            # Adjusting the weight of the edge based on the distances
            edge.y += initial_dist[u] - initial_dist[edge.x]

    distances = []
    for i in range(V):
        dist = dijkstras(new_graph, i)
        for j in range(V):
            if dist[j] != float('inf') and initial_dist[j] != float('inf'):
                # Adjusting the distances back after Dijkstra's algorithm
                dist[j] = dist[j] + initial_dist[j] - initial_dist[i]
        distances.append(dist)

    return distances


if __name__ == "__main__":
    graph = read_directed_graph()
    result = shortest_paths(graph)
    for row in result:
        print(" ".join('X' if path == float('inf') else str(path) for path in row))
