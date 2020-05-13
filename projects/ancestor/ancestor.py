from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id]= set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist in graph")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]
    
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s=Stack()
        s.push(starting_vertex)

        visited =set()

        while s.size()> 0:
            v= s.pop()
            if v not in visited:
                # print(v)
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)
        return(visited)
def earliest_ancestor(ancestors, starting_node):

    graph =Graph()

    # Add vertex
    s=1
    for i in range(len(ancestors)+1):
        graph.add_vertex(s)
        s+=1
    # Add edges
    for each_pair in ancestors:
        # print(each_pair[0],each_pair[1])
        graph.add_edge(each_pair[0],each_pair[1])
    
    s=1
    check=[]
    for ver in graph.vertices:
        
        if starting_node in graph.dft(ver):
            # print(len(graph.dft(ver)))
            if len(list(graph.dft(ver))) >1:
                print(ver)
                print(graph.dft(ver))
        #    if starting_node== graph.dft(ver):
        #        print(starting_node)
        #        break
        
        
if __name__ == '__main__':
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

    earliest_ancestor(test_ancestors,6  )