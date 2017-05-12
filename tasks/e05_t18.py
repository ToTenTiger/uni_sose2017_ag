from classes import DiGraph
from . import create_print_render_dot
from . import print_output_info


print("\nStart: Exercise 05 Task 18\n")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

inputs = ["a:b,d;b:;c:b;d:b;e:c,d;;",
          "a:b,c;b:e,d;c:d;d:;e:d,f;f:d,g;g:e;;",
          "a:;b:a;c:a;d:b,c,f;e:b,d;f:e;g:e,f;;"]

graphs = {}
for i, v in enumerate(inputs, start=1):
    graphs[i] = DiGraph(title="Exercise 05 Task 18 Graph 0{}".format(i),
                        filename="e05_t18_g0{}".format(i))
    graphs[i].read_input(value=v)
    dot_1 = create_print_render_dot(graphs[i])

results = {}
for i, graph in graphs.items():
    results[i] = (
        graph.top_sort_kahn(),
        graph.top_sort_tarjan()
    )

for i, (kahn, tarjan) in results.items():
    print("\nTopSort results of graph 0{}".format(i))
    print("Kahn:\t\t{}\n - visit order:\t{}".format(kahn[0], kahn[1]))
    print("Tarjan:\t\t{}\n - visit order:\t{}".format(tarjan[0], tarjan[1]) +
          "\n -- excludes loop of ancestor on visit of already visited nodes (find circle feature)")

print_output_info(e="05", t="18")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("\nEnd: Exercise 05 Task 18\n")
