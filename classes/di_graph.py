from itertools import filterfalse
from copy import deepcopy
import graphviz as gv

from .errors import FoundCircleError
from .errors import MultiEdgesNotAllowedError
from .edge import Edge
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
    # Exercise methods

    def top_sort_kahn(self):
        visit_seq = []
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
            visit_seq.append(current_node)
            to_so.append(current_node)
            for successor in self.get_neighbours_plus(current_node):
                visit_seq.append(successor)
                ein_grade[successor.node] -= 1
                if ein_grade[successor.node] <= 0:
                    ohne_vorgaenger.append(successor.node)
                    ein_grade.pop(successor.node)

        return to_so, visit_seq

    def top_sort_tarjan(self):
        visit_seq = []
        to_so = []
        visited = {}
        ohne_nachfolger = []

        for node in self.get_nodes():
            visited[node] = False
            aus_grad = self.aus_grad(node)
            if aus_grad <= 0:
                ohne_nachfolger.append(node)

        for current_node in ohne_nachfolger:
            try:
                self.top_sort_tarjan_visit(visit_seq, to_so, visited, current_node)
            except FoundCircleError:
                return None, visit_seq

        return to_so if len(to_so) > 0 else None, visit_seq

    def top_sort_tarjan_visit(self, visit_order, to_so, visited, node):
        visit_order.append(node)
        if not visited[node]:
            visited[node] = True
            for ancestor in self.get_neighbours_minus(node):
                self.top_sort_tarjan_visit(visit_order, to_so, visited, ancestor)
            to_so.append(node)
        else:
            # extension to determine existence of a circle
            for ancestor in self.get_neighbours_minus(node):
                if visited[ancestor]:
                    raise FoundCircleError

    def szhk(self):
        ds_nr = {}
        min_nr = {}
        count = 0
        deck = []

        for node in self.get_nodes():
            if node.node not in ds_nr:
                count = self.szhk_search(ds_nr, min_nr, count, deck, node)

        from classes import returnObject
        return returnObject(dict(depth=ds_nr, min=min_nr))

    def szhk_search(self, ds_nr, min_nr, count, deck, node):
        count += 1
        ds_nr[node.node] = count
        min_nr[node.node] = count
        deck.append(node)

        for successor in self.get_neighbours_plus(node):
            if successor.node not in ds_nr:
                count = self.szhk_search(ds_nr, min_nr, count, deck, successor)
                min_nr[node.node] = min(min_nr.get(node.node), min_nr.get(successor.node))
            elif successor in deck:
                min_nr[node.node] = min(min_nr.get(node.node), min_nr.get(successor.node))

        if ds_nr.get(node.node) == min_nr.get(node.node):
            szhk = []
            while True:
                cur_node = deck.pop()
                szhk.append(cur_node)
                if cur_node == node:
                    break
            print("Found strong correlation component (scc) in {}:".format(self.filename))
            print("\t|- Root\t: {}".format(szhk[-1]))
            print("\t|- scc\t: {}".format(szhk))
            print("\t|- dsNr\t: {}".format(ds_nr))
            print("\t|- minNr: {}".format(min_nr))

        return count

    def trans_conclusion_reduction(self):
        graph = deepcopy(self)
        graph_plus = deepcopy(self)
        graph_minus = deepcopy(self)

        from classes import returnObject
        result = returnObject(dict(
            graph=graph,
            graph_edges=len(graph.get_edges()),
            conclusion="<none>",
            conclusion_edges=-1,
            reduction="<none>",
            reduction_edges=-1))

        to_so = graph.top_sort_tarjan()
        if not to_so[0]:
            print("[DEBUG] No top. sort found.")
            return result

        for e in list(reversed(to_so[0])):  # reverse loop through top. sorted nodes
            top_sorted_successors_e = list(filterfalse(lambda n: n not in graph.get_neighbours_plus(e), to_so[0]))
            for y in top_sorted_successors_e:
                for z in graph_plus.get_neighbours_plus(y):
                    try:
                        graph_plus.add_edge(e, z)
                    except MultiEdgesNotAllowedError:
                        print("[DEBUG] Adding already existing edge is forbidden")  # TODO Why we even face this case?
                        pass
                for x in graph.get_neighbours_plus(e):
                    if to_so[0].index(x) < to_so[0].index(y) and graph_plus.has_edge(x, y):
                        graph_minus.remove_edge(e, y)

        result = returnObject(dict(
            graph=graph,
            graph_edges=len(graph.get_edges()),
            conclusion=graph_plus,
            conclusion_edges=len(graph_plus.get_edges()),
            reduction=graph_minus,
            reduction_edges=len(graph_minus.get_edges())))
        return result

    # ----------------------------------------------------------------
    # helper methods

    def has_edge(self, x: Edge, y: Edge):
        return (x, y) in self.get_edges()

    def find_msb(self):
        # TODO implement me
        raise NotImplementedError

    def kaZu_grad(self, node):
        return self.ein_grad(node)

    def kaZu_next_edge(self, u, edges):
        v = self.get_neighbours_plus(u)[0]
        edge = (u, v)
        if edges.count(edge) <= 0:
            edge = (v, u)
        return v, edge

    # ----------------------------------------------------------------
    # maybe not needed: after call a toDot call is needed

    def remove_edge(self, node, edge):
        x, y = node, edge
        if y not in self.adjazenz[x]:
            print("[DEBUG] Edge {} not exists".format((x, y)))
            return
        self.adjazenz[x].remove(y)

    # ----------------------------------------------------------------
    # unsupported methods

    def __eq__(self, other):
        raise NotImplementedError

    def __ne__(self, other):
        raise NotImplementedError
