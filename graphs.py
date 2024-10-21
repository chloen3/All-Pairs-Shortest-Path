import heapq

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]  # Adjusted for an extra vertex q
    for _ in range(m):
        u, v, c = map(int, input().split())
        graph[u].append((v, c))
    
    # Step 1: Add new vertex q and connect it to all vertices with edge weight 0
    for u in range(n):
        graph[n].append((u, 0))
    
    # Step 2: Run Bellman-Ford from new vertex to find minimum distances for reweighting
    dist = bellman_ford(graph, n + 1, n)
    if dist is None:
        print("Negative weight cycle detected")
        return

    # Step 3: Reweight the graph
    reweighted_graph = reweight_graph(graph, dist, n)
    
    # Step 4: Use Dijkstra's algorithm for each vertex on the reweighted graph
    all_pairs_dist = []
    for u in range(n):
        distances = dijkstra(reweighted_graph, u)
        all_pairs_dist.append(distances)
    
    # Print adjusted distances, ensuring 'X' is printed for unreachable vertices
    for row in all_pairs_dist:
        print(' '.join(str(dist) if dist != float('inf') else 'X' for dist in row))

def bellman_ford(graph, n, source):
    dist = [float('inf')] * n
    dist[source] = 0
    for _ in range(n - 1):
        for u in range(n):
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    
    # Check for negative weight cycles
    for u in range(n):
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                return None  # Negative cycle detected
    
    return dist

def reweight_graph(graph, dist, n):
    new_graph = [[] for _ in range(n)]
    for u in range(n):
        for v, w in graph[u]:
            if u < n and v < n:  # Skip edges from the added vertex q
                new_w = w + dist[u] - dist[v]
                new_graph[u].append((v, new_w))
    return new_graph

def dijkstra(graph, s):
    n = len(graph)
    distances = [float("inf")] * n
    distances[s] = 0
    queue = [(0, s)]
    
    while queue:
        p, u = heapq.heappop(queue)
        for v, cost in graph[u]:
            if p + cost < distances[v]:
                distances[v] = p + cost
                heapq.heappush(queue, (distances[v], v))
    
    return distances

if __name__ == "__main__":
    main()