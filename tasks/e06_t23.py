from classes import DiGraph
from . import create_print_render_dot
from . import print_output_info


print("\nStart: Exercise 06 Task 23\n")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

inputs = ["a:b,c,d;b:c;c:d;d:;;",
          "a:;b:c;c:a;d:c,a;;",
          "a:i,j;b:f,h;c:b,d;d:f,e,i,g;e:h,g;f:i,e;g:i,j,h;h:a;i:;j:i;k:c,b;;",
          "a:b;b:j;c:a;d:g,h;e:b,d;f:e,h;g:b,c;h:a,c;i:f,g,j;j:;;",
          "a:b;b:j;c:a;d:g,h;e:b,d;f:e,h;g:b,c;h:a,c;i:f,g,j;j:f;;"]
results = []
for i, adjazenzlist in enumerate(inputs, start=1):
    graph = DiGraph(title="Exercise 06 Task 23 Graph 0{}".format(i),
                    filename="e06_t23_g0{}".format(i),
                    value=adjazenzlist)
    results.append(graph.trans_conclusion_reduction())
    dot = create_print_render_dot(graph)

for i, r in enumerate(results, start=1):
    print("\n__Graph_0{}__________:\t{}".format(i, r.g))
    print(" - trans. conclusion:\t{}".format(r.c))
    print(" - trans. reduction :\t{}".format(r.r))

print_output_info(e="06", t="23")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("End: Exercise 06 Task 23\n")
