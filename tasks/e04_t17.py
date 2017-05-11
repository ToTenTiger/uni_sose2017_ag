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


create_print_render_dot(Graph(title="Exercise 04 Task 17 Graph 02",
                              filename="e04_t17_g02",
                              body=read_dot_body("tasks\e04_t17_g02.gv")))

create_print_render_dot(Graph(title="Exercise 04 Task 17 Graph 03",
                              filename="e04_t17_g03",
                              body=read_dot_body("tasks\e04_t17_g03.gv")))

create_print_render_dot(Graph(title="Exercise 04 Task 17 Graph 04",
                              filename="e04_t17_g04",
                              body=read_dot_body("tasks\e04_t17_g04.gv")))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("End: Exercise 04 Task 17")
