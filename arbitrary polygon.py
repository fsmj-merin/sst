# create a class with object vertices.
#This will give the nodes for the polygon. Each vertice contain x and y coordinates.
 # -----------------------------------------------------------------------------------------------------
class Vertex:

# Keep track of vertices as they are created
    vertex_count = 0
    vertex_list = []

# create a new vertex with default values
    def __init__(self):
        self.position=[0,0]
        self.id = Vertex.vertex_count
        Vertex.vertex_count = Vertex.vertex_count + 1
        Vertex.vertex_list.append(self)

# specify a string representation of a vertex
    def __str__(self):
        return 'Vertex %5d: (x0,y0) position (%f,%f)' % \
        (self.id, self.position[0], self.position[1])
    def Print(self):
        print(self)

v1=Vertex()
v1.position=[0,1]
v2=Vertex()
v2.position=[4,5]
print(Vertex.vertex_count)
print(Vertex.vertex_list[0])
    