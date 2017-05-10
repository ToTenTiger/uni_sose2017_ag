from classes import DiGraph
from . import create_print_render_dot


print("\nStart: Excise 05 Task 18\n")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

inputs = ["a:b,d;b:;c:b;d:b;e:c,d;;",
          "a:b,c;b:e,d;c:d;d:;e:d,f;f:d,g;g:e;;",
          "a:;b:a;c:a;d:b,c,f;e:b,d;f:e;g:e,f;;"]

graphs = {}
for i, v in enumerate(inputs, start=1):
    graphs[i] = DiGraph(title="Excise 05 Task 18 Graph 0{}".format(i),
                        filename="e05_t18_g0{}".format(i))
    graphs[i].read_input(value=v)
    dot_1 = create_print_render_dot(graphs[i])

results = {}
for i, graph in graphs.items():
    results[i] = (
        graph.top_sort_kahn(),
        graph.top_sort_tarjan()
    )

for i, r in results.items():
    print("\nTopSort results of graph 0{}".format(i))
    print("Kahn:\t{}".format(r[0]))
    print("Tarjan:\t{}".format(r[1]))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("\nEnd: Excise 05 Task 18\n")
