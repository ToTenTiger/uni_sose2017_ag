from ueb import *


class DiGraph(Graph):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

    def to_dot(self, allow_multi=True):
        self.dot = gv.Digraph(
            name=self.title,
            directory="graphs",
            filename=self.filename,
            strict=not self.allow_multi,
            graph_attr={},
            node_attr={},
            edge_attr={}
        )
        self._buildDot()
        return self.dot

    # ----------------------------------------------------------------
    # maybe not needed - after call a toGraph call is needed

    def remove_edge(self, node, edge):
        print("Not implemented yet")
        exit(1)

    # ----------------------------------------------------------------
    # not supported methods

    def hierholzer(self):
        print("Method hierholzer not supported for directed graphs")
        return

    # ----------------------------------------------------------------
    # supported methods

    def __eq__(self, other):
        return NotImplemented

    def __ne__(self, other):
        return NotImplemented
