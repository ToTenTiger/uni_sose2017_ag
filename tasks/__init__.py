import global_vars
from classes import *


def create_print_render_dot(graph):
    dot = graph.to_dot()

    if global_vars.printout:
        #answer = input("Options:Should I print the dot-file? [y/n]")
        #if not answer or answer == "y":
        print("\nYour graph G in dot format:\n{}\n".format(dot.source))

    dot.render(view=global_vars.view, cleanup=global_vars.cleanup)

    return dot

__all__ = ["Edge", "DiGraph", "Graph", "create_print_render_dot"]
