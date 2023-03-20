import sys
from collections import defaultdict
import heapq

# This class represents a directed graph
# using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def print(self):
        print(self.graph)

    # Function to print a BFS of graph
    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def BFS(self, s):
        queue = []
        trip = []
        visited = [False] * len(self.graph)

        queue.append(s)

        visited[s]= True

        while queue:
            node = queue.pop(0)
            trip.append(node)

            for neighbor in self.graph(node):
                if visited[neighbor] == False:
                    queue.append(neighbor)
                    visited[neighbor] = True

        return trip


    def DFS(self, s):
        stack = []
        visited = [False] * (len(self.graph))
        stack.append(s)

        while stack:
            x = stack.pop()
            if visited[x] == False:
                visited[x] = True
                print(x, end=" ")
                for i in self.graph[x]:
                    stack.append(i)

    def dijkstra(self, s):
        distances = {}
        for node in self.graph:
            distances[node] = sys.maxsize

        distances[s] = 0
        heap = [(0,s)]

        while heap:
            node, dist = heapq.heappop(heap)

            if dist > distances[node]:
                continue

            for neighbor, weight in self.graph[node]:
                distance = dist + weight

                if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappop(heap, (distance, neighbor))

        return distance


# Driver code

# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.addEdge(4, 1)
g.addEdge(1, 4)
g.addEdge(4, 2)
g.addEdge(2, 4)
g.addEdge(5, 3)
g.addEdge(3, 5)
g.print()
print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
g.BFS(2)
print("\n")
print("Following is Depth First Traversal"
      " (starting from vertex 2)")
g.DFS(2)
print("\n")
print("Following is Dijkstra"
      " (starting from vertex 2)")
g.dijkstra(2)