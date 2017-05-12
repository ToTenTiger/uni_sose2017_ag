from classes import Graph
from . import create_print_render_dot
from . import print_output_info


print("\nStart: Exercise 05 Task 19\n")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

graph = Graph(title="Exercise 05 Task 19 Graph 01",
              filename="e05_t19_g01")
graph.read_input(value="a:f;b:a;c:a,e;d:b,c,f;e:b,g;f:b;g:c,f;;")
dot = create_print_render_dot(graph)

print_output_info(e="05", t="19")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("\nEnd: Exercise 05 Task 19\n")
