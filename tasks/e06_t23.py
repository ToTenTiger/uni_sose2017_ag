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

print("Do you want to parse a file with 'ag' strings per line?")
file_request = input("Then enter a path > ")
if file_request:
    inputs.clear()
    file = open(file_request)
    for line in file:
        inputs.append(line)

results = []
for i, adjazenzlist in enumerate(inputs, start=1):
    graph = DiGraph(title="Exercise 06 Task 23 Graph 0{}".format(i),
                    filename="e06_t23_g0{}".format(i),
                    value=adjazenzlist,
                    allow_multi=True)
    print("Processing graph 0{} >>> Start <<<".format(i))
    r = graph.trans_conclusion_reduction()
    print("Processing graph 0{} >>> End <<<".format(i))
    results.append(r)
    create_print_render_dot(graph)
    if r.conclusion_edges > 0 and r.reduction_edges > 0:
        graph_plus = DiGraph(title="Exercise 06 Task 23 Graph 0{} (trans. conclusion))".format(i),
                             filename="e06_t23_g0{}_conc".format(i),
                             value=r.conclusion.to_string(),
                             allow_multi=True)
        create_print_render_dot(graph_plus)
        graph_minus = DiGraph(title="Exercise 06 Task 23 Graph 0{} (trans. reduction)".format(i),
                              filename="e06_t23_g0{}_redu".format(i),
                              value=str(r.reduction),
                              allow_multi=True)
        create_print_render_dot(graph_minus)

for i, r in enumerate(results, start=1):
    print("\n__Graph_0{}___________: (Edges={})\t{}".format(i, r.graph_edges, r.graph))
    if r.conclusion_edges > 0 and r.reduction_edges > 0:
        print(" - trans. conclusion : (Edges={})\t{}".format(r.conclusion_edges, r.conclusion))
        print(" - trans. reduction  : (Edges={})\t{}".format(r.reduction_edges, r.reduction))
    else:
        print(" [WARN] No top. sort : found circle!")

print_output_info(e="06", t="23")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("End: Exercise 06 Task 23\n")
