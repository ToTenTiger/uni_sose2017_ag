from ueb.graph import Graph


graph = Graph(title="Excise 01 graph 02",
              filename="01-02",
              allow_multi=True)
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

dot = graph.to_dot()
#print(dot.source)
dot.render(view=1, cleanup=1)
print("Hierholzer Output: {}".format(graph.hierholzer()))
