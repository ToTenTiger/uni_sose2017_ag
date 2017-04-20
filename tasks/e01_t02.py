from tasks import *

print("Start: Excise 01 Task 02")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

graph = DiGraph(title="Excise 01 Task 02 Graph 01",
                filename="e01_t02_g01",
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

dot = create_print_render_dot(graph)

print("Hierholzer-Folge: {}".format(graph.hierholzer()))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("End: Excise 01 Task 02")
