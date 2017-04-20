from classes import *


def create_print_render_dot(graph: Graph, ask_to_print=True, view=True, cleanup=True):
    dot = graph.to_dot()

    if ask_to_print:
        answer = input("Should I print the dot-file? [y/n]")
        if not answer or answer == "y":
            print("\nYour graph G in dot format:\n{}\n".format(dot.source))

    dot.render(view=view, cleanup=cleanup)

    return dot

__all__ = ["Edge", "DiGraph", "Graph", "create_print_render_dot"]
