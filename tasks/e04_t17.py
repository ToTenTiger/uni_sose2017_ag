from os.path import join as get_path

from classes import Graph
from . import create_print_render_dot
from . import read_dot_body


print("Start: Exercise 04 Task 17")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

graph = Graph(title="Exercise 04 Task 17 Graph 01",
              filename="e04_t17_g01")
graph.read_input(value="a:b,h,e;" +
                       "b:g,c,e,a;" +
                       "c:h,b;" +
                       "d:f,e,g;" +
                       "e:a,b,d;" +
                       "f:d,h;" +
                       "g:b,d;" +
                       "h:c,a,f;;")
dot = create_print_render_dot(graph)

files = ["e04_t17_g02", "e04_t17_g03", "e04_t17_g04"]
for i, file in enumerate(files, start=2):
    create_print_render_dot(
        Graph(title="Exercise 04 Task 17 Graph 0{}".format(i),
              filename="e04_t17_g0{}".format(i),
              body=read_dot_body(get_path("tasks", "e04_t17_g0{}.gv".format(i)))))

print("\nGraphs has been generated under directory 'graphs'." +
      "\nFile name pattern e04_t17_g<NUMBER>\n")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("End: Exercise 04 Task 17")
