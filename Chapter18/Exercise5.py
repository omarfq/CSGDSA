# Write a function that accepts two vertices from an unweighted graph and retus the shortest
# path between them.
class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []

    def add_adjacent_vertex(self, *vertices):
        for vertex in vertices:
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


def find_shortest_path(first_vertex, second_vertex, visited_vertices={}):
    queue = Queue()

    # As in Dijkstra's algorithm, we keep track in a table of each vertex's
    # immediately preceeding vertex
    previous_vertex_table = {}

    # We employ BFS
    visited_vertices[first_vertex.value] = True
    queue.enqueue(first_vertex)

    while not queue.is_empty():
        current_vertex = queue.dequeue()
        for adjacent_vertex in current_vertex.adjacent_vertices:
            if adjacent_vertex.value not in visited_vertices:
                visited_vertices[adjacent_vertex.value] = True
                queue.enqueue(adjacent_vertex)

                # We store in the previous_vertex_table the adjacent_vertex as the key,
                # and the current_vertex as the value. This indicates that the current_vertex
                # is the immediately preceeding vertex that leads to the adjacent_vertex
                previous_vertex_table[adjacent_vertex.value] = current_vertex.value

    # As in Dijkstra's Algorithm, we work backwards through the previous vertex table
    # to build the shortest path
    shortest_path = []
    current_vertex_value = second_vertex.value

    while current_vertex_value != first_vertex.value:
        shortest_path.append(current_vertex_value)
        current_vertex_value = previous_vertex_table[current_vertex_value]

    shortest_path.append(first_vertex.value)
    return shortest_path[::-1]


idris = Vertex('Idris')
kamil = Vertex('Kamil')
lina = Vertex('Lina')
sasha = Vertex('Sasha')
marco = Vertex('Marco')
ken = Vertex('Ken')
talia = Vertex('Talia')

idris.add_adjacent_vertex(kamil, talia)
kamil.add_adjacent_vertex(idris, lina)
lina.add_adjacent_vertex(kamil, sasha)
sasha.add_adjacent_vertex(lina, marco)
marco.add_adjacent_vertex(sasha, ken)
ken.add_adjacent_vertex(marco, talia)
talia.add_adjacent_vertex(ken, idris)

print(find_shortest_path(idris, lina))
