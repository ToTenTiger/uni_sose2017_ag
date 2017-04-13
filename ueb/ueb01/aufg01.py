from ueb.di_graph import DiGraph


graph = DiGraph(title="Excise 01 graph 01",
                filename="01-01")
graph.read_input(value="0:2,3,5,7;" +
                       "1:3,4,5,6;" +
                       "2:0,6,7,9;" +
                       "3:0,1,8,10;" +
                       "4:1,5,5,8;" +
                       "5:0,1,4,4,8,10;" +
                       "6:1,2,8,9;" +
                       "7:0,2,9,10;" +
                       "8:3,4,5,6;" +
                       "9:2,6,7,10;" +
                       "10:3,5,7,9;;")

print("bnb(2,4) ? %s" % graph.bnb("2", "4"))
print("bnb(4,2) ? %s" % graph.bnb("4", "2"))

print("ausGrad(2) ? %s" % graph.aus_grad("2"))
print("ausGrad(8) ? %s" % graph.aus_grad("8"))
print("einGrad(7) ? %s" % graph.ein_grad("7"))
print("einGrad(2) ? %s" % graph.ein_grad("2"))
print("grad(10) ? %s" % graph.grad("10"))

dot = graph.to_graph()
#print(dot.source)
dot.render(view=1, cleanup=1)
