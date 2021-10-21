# Implementation of the BFS Algorithm
class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []

    def add_adjacent_vertex(self, vertex):
        if vertex in self.adjacent_vertices:
            return
        self.adjacent_vertices.append(vertex)
        self.add_adjacent_vertex(vertex)


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0


def bfs_traversal(starting_vertex):
    queue = Queue()

    visited_vertices = {}
    visited_vertices[starting_vertex.value] = True
    queue.enqueue(starting_vertex)

    # While the queue is not empty
    while not queue.is_empty():
        # Remove the first vertex off the queue and make it the current vertex
        current_vertex = queue.dequeue()

        # Print the current vertex's value
        print(current_vertex.value)

        # Iterate over current vertex's adjacent vertices
        for adjacent_vertex in current_vertex.adjacent_vertices:
            # If we have not visited the adjacent vertex
            if adjacent_vertex.value not in visited_vertices:
                # Mark the adjacent vertex as visited
                visited_vertices[adjacent_vertex.value] = True

                # Add the adjacent vertex to the queue
                queue.enqueue(adjacent_vertex)


alice = Vertex('Alice')
bob = Vertex('Bob')
cynthia = Vertex('Cynthia')

alice.add_adjacent_vertex(bob)
alice.add_adjacent_vertex(cynthia)
bob.add_adjacent_vertex(cynthia)
cynthia.add_adjacent_vertex(bob)

bfs_traversal(alice)
