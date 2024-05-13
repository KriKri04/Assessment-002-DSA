class Vertex:
    def __init__(self, key) -> None:
        self.key = key

        # variables for bfs
        self.parent = None
        self.color = 'white'
        self.distance = 0

    def __repr__(self) -> str:
        return repr(str(self.key))


class Edge:
    def __init__(self, source, destination, like, comment) -> None:
        self.source = source
        self.destination = destination
        self.like = like 
        self.comment = comment
    
    def __repr__(self) -> str:
        return f"{self.source} {self.destination}, {self.like}, {self.comment}"


class Graph:
    def __init__(self, directed=False) -> None:
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        return self._incoming is not self._outgoing
    
    def add_vertex(self, key):
        if key in self._outgoing:
            print("Error: vertex already in graph")
            return False
        else:
            v = Vertex(key)
            self._outgoing[v] = {}

            if self.is_directed():
                self._incoming[v] = {} 
            return v
        
    def add_edge(self, source, destination, like, comment):
        u_vertex = None
        v_vertex = None
        
        for vertex in self.vertices():
            if vertex.key == source:
                u_vertex = vertex
            elif vertex.key == destination:
                v_vertex = vertex

        edge = Edge(u_vertex, v_vertex, like, comment)
        self._outgoing[u_vertex][v_vertex] = edge
        self._incoming[v_vertex][u_vertex] = edge

    def vertices(self):
        return self._outgoing.keys()

    def display(self):
        for key in self._outgoing:
            print(self._outgoing[key])

    def get_total_likes(self, user):
        incoming_edges = self._incoming[user]
        # print(incoming_edges)
        likes = 0

        for edge in incoming_edges.values():
            likes = likes + edge.like

        return likes

    def get_total_comments(self, user):
        incoming_edges = self._incoming[user]
        comments = 0

        for edge in incoming_edges.values():
            comments = comments + edge.comment

        return comments 
    
    def get_followers(self, user):
        return len(self._incoming[user])
    
    def engagement_rate(self, user):
        return (self.get_total_likes(user) + self.get_total_comments(user)) / self.get_followers(user) * 100
    
    def shortest_path(self, source_key, destination_key):
        # Initialize BFS
        visited = {}
        path = {}  # To store the path taken to reach each vertex
        for vertex in self.vertices():
            visited[vertex] = False
            path[vertex] = None

        queue = []
        source_vertex = None
        destination_vertex = None
        for vertex in self.vertices():
            if vertex.key == source_key:
                source_vertex = vertex
            elif vertex.key == destination_key:
                destination_vertex = vertex

        if source_vertex is None or destination_vertex is None:
            print("Error: Source or destination vertex not found")
            return None, None

        queue.append((source_vertex, 0))  # (vertex, distance)
        visited[source_vertex] = True

        # BFS traversal
        while queue:
            current_vertex, distance = queue.pop(0)
            if current_vertex == destination_vertex:
                # Reconstruct the path
                path_taken = []
                while current_vertex is not None:
                    path_taken.insert(0, current_vertex)
                    current_vertex = path[current_vertex]
                return distance, path_taken  # Found shortest path and path taken
            for neighbor_vertex in self._outgoing[current_vertex]:
                if not visited[neighbor_vertex]:
                    queue.append((neighbor_vertex, distance + 1))
                    visited[neighbor_vertex] = True
                    path[neighbor_vertex] = current_vertex  # Store the path

        print("Error: No path found between source and destination")
        return None, None

    def get_incoming_edges(self, vertex):
        return self._incoming[vertex]
    
    def get_likes(self, source_vertex, destination_vertex):
        edges = self.get_incoming_edges(destination_vertex)
        for edge in edges.values():
            if edge.source ==  source_vertex:
                return edge.like
            
    def get_comments(self, source_vertex, destination_vertex):
        edges = self.get_incoming_edges(destination_vertex)
        for edge in edges.values():
            if edge.source ==  source_vertex:
                return edge.comment
            
    def influence_formula(self, source_vertex, destination_vertex):
        return (self.get_likes(source_vertex, destination_vertex) + self.get_comments(source_vertex, destination_vertex)) / self.engagement_rate(source_vertex)

    def highest_engagement(self, source_key, destination_key):
        # Initialize distance to all vertices as infinity
        distances = {vertex: float('-inf') for vertex in self.vertices()}
        distances[source_key] = 0  # Distance from source to source is 0

        # Initialize a priority queue (min heap) to keep track of vertices and their distances
        pq = [(0, source_key)]  # (distance, vertex)
        path = {}
        visited = set()

        while pq:
            # Get the vertex with the smallest distance from the priority queue
            pq.sort(key=lambda x: x[0])
            current_distance, current_vertex = pq.pop()

            # Skip if the vertex has already been visited
            if current_vertex in visited:
                continue
            visited.add(current_vertex)

            # If the current vertex is the destination, reconstruct and return the path
            if current_vertex == destination_key:
                shortest_path = []
                while current_vertex is not None:
                    shortest_path.insert(0, current_vertex)
                    current_vertex = path.get(current_vertex)
                return distances[destination_key], shortest_path

            # Visit all neighboring vertices
            for neighbor_vertex in self._outgoing[current_vertex]:
                edge = self._outgoing[current_vertex][neighbor_vertex]
                # Calculate the distance to the neighbor through the current vertex
                distance_to_neighbor = current_distance + self.influence_formula(current_vertex, neighbor_vertex)
                # If the influence level is greater than the recorded influence level to the neighbor, update it
                if distance_to_neighbor > distances[neighbor_vertex]:
                    distances[neighbor_vertex] = distance_to_neighbor
                    path[neighbor_vertex] = current_vertex
                    pq.append((distance_to_neighbor, neighbor_vertex))

        print("Error: No path found between source and destination")
        return None, None
    

   
if __name__ == "__main__":


    graph = Graph(directed=True)

    keys = ['s', 't', 'y', 'x', 'z']

    edges = [ ['s', 't', 1000, 10000], ['s', 'y', 5, 4], ['t', 'x', 1, 3], ['t', 'y', 2, 5], ['y', 't', 3, 6], ['y', 'x', 9, 8], 
              ['y', 'z', 2, 4], ['z', 's', 7, 5], ['x', 'z', 4, 1], ['z', 'x', 6, 7]
            ]
    # edges = [ ['s', 't', 10]
    #         ]
    vertices = {}
    for key in keys:
        vertex = graph.add_vertex(key)
        vertices[key] = vertex

    for edge in edges:
        graph.add_edge(edge[0], edge[1], edge[2], edge[3])
    # graph.display()


    print("Outgoing")
    print(graph._outgoing)

    print("Incoming")
    print(graph._incoming)

    print('Likis')
    print(graph.get_total_likes(vertices['s']))

    print('Comentos')
    print(graph.get_total_comments(vertices['s']))
    print(graph.get_followers(vertices['s']))

    print('engagement rate')
    print(graph.engagement_rate(vertices['s']))

     # Find shortest path between 's' and 'y'
    shortest_path_length = graph.shortest_path('s', 'y')
    if shortest_path_length is not None:
        print(f"Shortest path length between 's' and 'y': {shortest_path_length}")

    print('get likes')
    print(graph.get_likes(vertices['s'], vertices['y']))

    print('get comments')
    print(graph.get_comments(vertices['s'], vertices['y']))

    print('influence formula')
    print(graph.influence_formula(vertices['s'], vertices['y']))

    print('highest engagement')
    print(graph.highest_engagement(vertices['s'], vertices['y']))
