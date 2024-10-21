All-Pairs Shortest Path Algorithm using Johnson's Algorithm
This project implements an all-pairs shortest path algorithm using Johnson's Algorithm, which combines Bellman-Ford and Dijkstra's algorithms. This approach allows efficient shortest path calculation even when negative edge weights are present (as long as there are no negative cycles).

Algorithm Overview
Input:

A weighted, directed or undirected graph with n vertices and m edges.
Vertices can have negative weights, but there must be no negative weight cycles.
Steps:

Step 1: Add an extra vertex to the graph, connect it to all other vertices with edge weight 0.
Step 2: Use Bellman-Ford to detect negative cycles and compute potential values for reweighting the graph.
Step 3: Reweight the graph using the results of Bellman-Ford to ensure all edge weights are non-negative.
Step 4: Apply Dijkstra's algorithm from each vertex to find the shortest paths in the reweighted graph.
Step 5: Adjust the shortest path results back to the original graph's weights.
Output:

The shortest path distances between every pair of vertices. If a vertex is unreachable, 'X' is printed.