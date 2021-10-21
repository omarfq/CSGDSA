# Implementation of the DFS Algorithm
class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []

    def add_adjacent_vertex(self, vertex):
        if vertex in self.adjacent_vertices:
            return
        self.adjacent_vertices.append(vertex)
        self.add_adjacent_vertex(vertex)


def dfs_traversal(vertex, visited_vertices={}):
    # Mark vertex as visited by adding it to the hash table
    visited_vertices[vertex.value] = True

    # Print the vertex's value
    print(vertex.value)

    # Iterate through the current vertex's adjacen vertices
    for adjacent_vertex in vertex.adjacent_vertices:
        # Ignore an adjacent vertex if we've already visited it
        if adjacent_vertex.value in visited_vertices:
            continue

        # Recursively call this method on the adjacent vertex
        dfs_traversal(adjacent_vertex, visited_vertices)


alice = Vertex('Alice')
bob = Vertex('Bob')
cynthia = Vertex('Cynthia')

alice.add_adjacent_vertex(bob)
alice.add_adjacent_vertex(cynthia)
bob.add_adjacent_vertex(cynthia)
cynthia.add_adjacent_vertex(bob)

dfs_traversal(alice)
