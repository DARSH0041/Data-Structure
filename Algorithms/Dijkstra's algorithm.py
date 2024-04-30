import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, v1, v2, weight):
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1].append((v2, weight))
            # For undirected graph, uncomment the line below
            # self.graph[v2].append((v1, weight))

    def dijkstra(self, start):
        distances = {vertex: float('inf') for vertex in self.graph}
        #print(distances)
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

# Example usage:
graph = Graph()
graph.add_node(0)
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)
graph.add_node(5)
graph.add_node(6)
graph.add_edge(0, 1, 2)
graph.add_edge(0, 2, 6)
graph.add_edge(1, 3, 5)
graph.add_edge(2, 3, 8)
graph.add_edge(3, 4, 10)
graph.add_edge(3, 5, 15)
graph.add_edge(4, 6, 2)
graph.add_edge(4, 6, 6)

start_node = 0
end_node = 4
print(graph.graph)
shortest_distances = graph.dijkstra(start_node)
shortest_path_length = shortest_distances[end_node]
print(shortest_distances)
print(f"The shortest path from node {start_node} to node {end_node} is {shortest_path_length}.")
