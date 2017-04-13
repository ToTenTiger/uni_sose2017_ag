from ueb.graph import Graph

graph = Graph(title="Excise 08 graph 01",
              filename="08-01",
              allow_multi=False,
              weighted=True)
graph.read_input(value="0:2-2,3-4.5,5-4,7-4.5;" +
                       "1:3-2.5,4-2,5-2,6-2.5;" +
                       "2:0-2.5,6-2,7-2,9-3;" +
                       "3:0-4,1-2,8-3,10-4.5;" +
                       "4:1-2,5-2,8-2;" +
                       "5:0-3,1-2,4-2.5,8-3,10-5;" +
                       "6:1-3,2-2,8-3,9-2;" +
                       "7:0-5,2-2.5,9-2,10-4.5;" +
                       "8:3-3,4-2,5-2,6-3;" +
                       "9:2-3,6-2,7-2,10-3;" +
                       "10:3-4,5-3.5,7-4.5,9-3;;")

dot = graph.to_dot()
# print(dot.source)
dot.render(view=1, cleanup=1)
