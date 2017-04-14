from classes import *


graph = DiGraph(title="test graph",
                filename="test01")
graph.read_input(value="A:B,C;C:C;")

dot = graph.to_dot()
print("Your graph G in dot format:\n{}".format(dot.source))
dot.render(view=1, cleanup=1)

print("K(G) ? {}".format(graph.get_edges()))

print("N(A) ? {}".format(graph.get_neighbours("A")))
print("N+(A) ? {}".format(graph.get_neighbours_plus("A")))
print("N-(A) ? {}".format(graph.get_neighbours_minus("A")))
print("d(A) ? {}".format(graph.grad("A")))
print("d+(A) ? {}".format(graph.aus_grad("A")))
print("d-(A) ? {}".format(graph.ein_grad("A")))

print("bnb(B, A) ? {}".format(graph.bnb("B", "A")))
print("bnb(B, C) ? {}".format(graph.bnb("B", "C")))

