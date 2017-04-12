from ueb.graph import Graph


graph = Graph(title="Excise 01 graph 01",
              filename="01-01")
graph.readInput(value="1:2,3,5,10;2:3,4,7,8;3:5;4:7,10;5:6,8,10;6:7,8,9;7:9,11;8:10;9:10,11;10:11;11:;;")

print("bnb(2,4) ? %s" % graph.bnb("2", "4"))
print("bnb(4,2) ? %s" % graph.bnb("4", "2"))

print("ausGrad(2) ? %s" % graph.ausGrad("2"))
print("ausGrad(8) ? %s" % graph.ausGrad("8"))
print("einGrad(7) ? %s" % graph.einGrad("7"))
print("einGrad(2) ? %s" % graph.einGrad("2"))
print("grad(10) ? %s" % graph.grad("10"))

dot = graph.toDiGraph()
#print(dot.source)
dot.render(view=1, cleanup=1)
