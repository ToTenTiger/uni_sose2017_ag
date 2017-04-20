import graphviz as gv

from .graph import Graph


class DiGraph(Graph):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

    def to_dot(self):
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
    # helper methods

    def kaZu_grad(self, node):
        return self.ein_grad(node)

    def kaZu_next_edge(self, u, edges):
        v = self.get_neighbours_plus(u)[0]
        edge = (u, v)
        if edges.count(edge) <= 0:
            edge = (v, u)
        return v, edge

    # ----------------------------------------------------------------
    # maybe not needed - after call a toGraph call is needed

    def remove_edge(self, node, edge):
        x, y = node, edge
        if y not in self.adjazenz[x] :
            print("Edge {} not exists".format((x, y)))
            return
        self.adjazenz[x].remove(y)

    # ----------------------------------------------------------------
    # unsupported methods

    def __eq__(self, other):
        return NotImplemented

    def __ne__(self, other):
        return NotImplemented
