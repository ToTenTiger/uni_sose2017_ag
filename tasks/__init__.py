import global_vars


def create_print_render_dot(graph):
    dot = graph.to_dot()

    if global_vars.printout:
        #answer = input("Options:Should I print the dot-file? [y/n]")
        #if not answer or answer == "y":
        print("\nYour graph G in dot format:\n{}\n".format(dot.source))

    dot.render(view=global_vars.view, cleanup=global_vars.cleanup)

    return dot


def read_dot_body(filepath):
    return open(filepath).readlines()[1:-1]


def print_output_info(e, t):
    print("\nGraph(s) has been generated under directory 'graphs'." +
          "\nFile name pattern e{}_t{}_g<NUMBER>\n".format(e, t))
