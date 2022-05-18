from DijkstraAlgorithm import Node, Graph

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")

graph = Graph.create_from_nodes([a, b, c, d, e, f])

graph.connect(a, b, 4)
graph.connect(a, c, 7)
graph.connect(a, e, 1)
graph.connect(b, c, 4)
graph.connect(b, d, 2)
graph.connect(c, d, 8)
graph.connect(c, f, 10)
graph.connect(d, e, 6)

print([(weight, [n.data for n in node]) for (weight, node) in graph.dijkstra(b)])