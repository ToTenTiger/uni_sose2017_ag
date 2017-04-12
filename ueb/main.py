from ueb.graph import Graph

adjazenz = {
    "A": ["B", "C"],
    "B": [],
    "C": ["C"]
}
graph = Graph(title="test graph",
              filename="01-01",
              adjazenzlist=adjazenz)
print("bnb(C, A) ? %s" % graph.bnb("C", "A"))
print("bnb(C, B) ? %s" % graph.bnb("C", "B"))
dot = graph.toGraph(directional=True)
print(dot.source)
dot.render(view=0, cleanup=1)
