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
    # excise methods

    def top_sort_kahn(self):
        to_so = []
        ohne_vorgaenger = []
        ein_grade = {}

        for node in self.get_nodes():
            ein_grad = self.ein_grad(node)
            if ein_grad > 0:
                ein_grade[node] = ein_grad
            else:
                ohne_vorgaenger.append(node)

        while ohne_vorgaenger:
            current_node = ohne_vorgaenger.pop(0)
            to_so.append(current_node)
            for successor in self.get_neighbours_plus(current_node):
                ein_grade[successor.node] -= 1
                if ein_grade[successor.node] <= 0:
                    ohne_vorgaenger.append(successor.node)
                    ein_grade.pop(successor.node)

        return to_so

    def top_sort_tarjan(self):
        to_so = []
        visited = {}
        ohne_nachfolger = []

        for node in self.get_nodes():
            visited[node] = False
            aus_grad = self.aus_grad(node)
            if aus_grad <= 0:
                ohne_nachfolger.append(node)

        for current_node in ohne_nachfolger:
            self.top_sort_tarjan_visit(to_so, visited, current_node)

        return to_so

    def top_sort_tarjan_visit(self, to_so, visited, node):
        if not visited[node]:
            visited[node] = True
            for ancestor in self.get_neighbours_minus(node):
                self.top_sort_tarjan_visit(to_so, visited, ancestor)
            to_so.append(node)

    # ----------------------------------------------------------------
    # helper methods

    def find_msb(self):
        # TODO implement me
        exit("Not implemented yet")

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
