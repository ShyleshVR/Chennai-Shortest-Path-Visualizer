import heapq

def dijkstra(graph, start):
     # Initialize distances to infinity
    distances = {node: float('inf') for node in graph}
    # Distance from start to start is 0
    distances[start] = 0
    # Priority queue to store nodes with their distances
    pq = [(0, start)]
    # Predecessors dictionary to keep track of the predecessors of each node
    predecessors = {}
    
    while pq:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(pq)
        
        # If we have already found a shorter path to this node, skip
        if current_distance > distances[current_node]:
            continue
        
        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # If we found a shorter path to neighbor, update distance and push to queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    return distances, predecessors

def shortest_path(graph, start, destination):
    distances, predecessors = dijkstra(graph, start)
    path = []
    current_node = destination
    while current_node != start:
        path.insert(0, current_node)
        current_node = predecessors[current_node]
    path.insert(0, start)
    return path