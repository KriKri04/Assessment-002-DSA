# Social Network Graph Implementation

## Overview
This project implements a directed graph to represent a social network, where members can follow each other, like posts, and comment on them. The graph structure supports the following functionalities:
- Adding vertices (members)
- Adding edges (connections between members with likes and comments)
- Calculating the engagement rate of each member
- Finding the shortest path between any two members
- Calculating influence between members

## Classes and Methods

### Class `Vertex`
Represents a member in the social network.
- `__init__(self, key)`: Initializes a vertex with a unique key.
- `__repr__(self)`: Returns a string representation of the vertex.

### Class `Edge`
Represents a connection between two members, including likes and comments.
- `__init__(self, source, destination, like, comment)`: Initializes an edge with source, destination, likes, and comments.
- `__repr__(self)`: Returns a string representation of the edge.

### Class `Graph`
Represents the social network as a graph.
- `__init__(self, directed=False)`: Initializes the graph, which can be directed or undirected.
- `is_directed(self)`: Checks if the graph is directed.
- `add_vertex(self, key)`: Adds a vertex to the graph.
- `add_edge(self, source, destination, like, comment)`: Adds an edge to the graph.
- `vertices(self)`: Returns all vertices in the graph.
- `display(self)`: Displays all edges in the graph.
- `get_total_likes(self, user)`: Returns the total likes received by a user.
- `get_total_comments(self, user)`: Returns the total comments received by a user.
- `get_followers(self, user)`: Returns the number of followers a user has.
- `engagement_rate(self, user)`: Calculates the engagement rate of a user.
- `shortest_path(self, source_key, destination_key)`: Finds the shortest path between two members using BFS.
- `get_incoming_edges(self, vertex)`: Returns all incoming edges for a vertex.
- `get_likes(self, source_vertex, destination_vertex)`: Returns likes from one member to another.
- `get_comments(self, source_vertex, destination_vertex)`: Returns comments from one member to another.
- `influence_formula(self, source_vertex, destination_vertex)`: Calculates the influence of one member on another.
- `highest_engagement(self, source_key, destination_key)`: Finds the path with the highest engagement between two members.

## Usage

### Adding Vertices and Edges
To add members and their connections:
```python
graph = Graph(directed=True)
keys = ['s', 't', 'y', 'x', 'z']
for key in keys:
    graph.add_vertex(key)

edges = [
    ['s', 't', 1000, 10000], ['s', 'y', 5, 4], ['t', 'x', 1, 3], 
    ['t', 'y', 2, 5], ['y', 't', 3, 6], ['y', 'x', 9, 8], 
    ['y', 'z', 2, 4], ['z', 's', 7, 5], ['x', 'z', 4, 1], ['z', 'x', 6, 7]
]
for edge in edges:
    graph.add_edge(edge[0], edge[1], edge[2], edge[3])
```
## Calculating Engagement Rate

To calculate the engagement rate of a member:

```python
engagement_rate = graph.engagement_rate(vertices['s'])
print(f"Engagement rate: {engagement_rate}")
```

## Finding The Shortest Path

```python
distance, path = graph.shortest_path('s', 'y')
if path is not None:
    print(f"Shortest path: {path}")
```

## Calculating Influence

To calculate the influence of one member on another:

```python
influence = graph.influence_formula(vertices['s'], vertices['y'])
print(f"Influence: {influence}")
```

## Finding the Path with the Highest Engagement

To find the path with the highest engagement between two members:

```python
engagement, path = graph.highest_engagement(vertices['s'], vertices['y'])
if path is not None:
    print(f"Path with highest engagement: {path}")
```

## Running the Code
To run the code, execute the script in a Python environment. The provided example in the if `__name__ == "__main__":` block demonstrates how to initialize the graph, add vertices and edges, and perform various calculations.