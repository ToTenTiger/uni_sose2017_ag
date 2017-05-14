from copy import deepcopy
from re import compile as regex_compile
from typing import List

import graphviz as gv
from graphviz.dot import Dot

import global_vars
from .edge import Edge


class Graph:
    def __init__(self,
                 title=None,
                 filename: str="graph",
                 body=None,
                 adjazenzdict: dict=None,
                 allow_multi=False,
                 weighted=False,
                 value=None):
        self.dot = Dot()

        self.title = title
        self.filename = filename if filename.endswith(".gv") else filename + ".gv"
        self.body = body
        self.adjazenz = adjazenzdict if adjazenzdict else dict()
        self.allow_multi = allow_multi
        self.weighted = weighted
        if not adjazenzdict and value:
            self.read_input(value)

    def read_input(self, value=None, text="Insert graph input string :> ", onfly_allowed=True):
        self.clear()
        raw_input = value
        if not value:
            raw_input = input(text)
        elif onfly_allowed and global_vars.onflygraph:
            print("\nUsing passed adjazenz list: {}\n".format(value))
            new_input = input("Enter any other list to use or press [Enter] to continue: ")
            if new_input:
                raw_input = new_input

        if not self.weighted:
            pattern = regex_compile("(\w+):(\w+|[\w,]*);")
            for (node, edges) in pattern.findall(raw_input):
                edge_list = str(edges).split(",")
                self.add_node(node, [])
                # converts list<str> on the fly to list<Edge>
                # list+filter contruct to ignor empty entries
                self.add_edges(node, [Edge(e) for e in list(filter(None, edge_list))])
        else:
            pattern_nodes = regex_compile("(\w+):(|(?:\w+-\d+(?:\.\d+)?)(?:,\w+-\d+(?:\.\d+)?)*);")
            pattern_edges = regex_compile("(\d+)-(\d+(?:\.\d+)?)")
            for (node, edges) in pattern_nodes.findall(raw_input):
                self.add_node(node, [])
                for (edge, weight) in pattern_edges.findall(edges):
                    e = Edge(edge, weight)
                    self.add_edge(node, e)

    def to_dot(self):
        self.dot = gv.Graph(
            name=self.title,
            directory="graphs",
            filename=self.filename,
            strict=not self.allow_multi,
            graph_attr={},
            node_attr={},
            edge_attr={},
            body=self.body
        )

        if not self.body:
            self._buildDot()
        return self.dot

    # ----------------------------------------------------------------
    # helper methods

    def clear(self):
        self.adjazenz.clear()

    def get_neighbours_plus(self, node):
        return list(map(
            lambda e: Edge(e),
            self.adjazenz.get(str(node))
        )) or []

    def get_neighbours_minus(self, node):
        neighbours = []
        for n, es in self.adjazenz.items():
            for e in es:
                if e == str(node):
                    neighbours.append(Edge(n, e.weight))
        return neighbours

    def get_neighbours(self, node):
        return self.get_neighbours_plus(node) + self.get_neighbours_minus(node)

    def get_edges(self):
        K = []
        for node in self.adjazenz.keys():
            for edge in self.get_neighbours_plus(node):
                K.append((node, edge))
        return deepcopy(K)

    def get_nodes(self):
        E = []
        for node in self.adjazenz.keys():
            E.append(Edge(node))
        return E

    def kaZu_grad(self, node):
        return self.grad(node)

    def kaZu_next_edge(self, u, edges):
        v = self.get_neighbours(u)[0]
        edge = (u, v)
        if edges.count(edge) <= 0:
            edge = (v, u)
        return v, edge

    # ----------------------------------------------------------------
    # 'protected' methods

    def _buildDot(self):
        for node, edges in self.adjazenz.items():
            self.dot.node(node)
            for edge in edges:
                label = str(edge.weight) if self.weighted else None
                self.dot.edge(node, edge.node, label)

    # ----------------------------------------------------------------
    # Exercise methods

    def bnb(self, x, y):
        return y in self.get_neighbours_plus(x) or x in self.get_neighbours_plus(y)

    def aus_grad(self, x):
        return len(self.get_neighbours_plus(x))

    def ein_grad(self, x):
        return len(self.get_neighbours_minus(x))

    def grad(self, x):
        return self.aus_grad(x) + self.ein_grad(x)

    def hierholzer(self):
        if self.dot.strict:
            print("Method hierholzer not supported for graphs without cycles")
            return

        d = []  # liste von allen eckengraden
        ung = []  # liste von ecken mit ungeradem grad
        for node in self.adjazenz.keys():
            grad = self.grad(node)
            d.append(grad)
            if grad % 2 == 1:
                ung.append(node)

        if 0 in d:
            print("Kein Euler-KaZu, der Graph ist nicht zh")
            return False
        if len(ung) > 2 or len(ung) == 1:
            print("Kein Euler-KaZu, > 2 oder 1 Ecke(n) mit ung. Grad")
            return False

        u = next(iter(self.adjazenz.keys()))
        ziel = u
        if len(ung) == 2:
            u, ziel = ung

        return self.kaZu(u, ziel)

    def kaZu(self, x, y):
        graph = deepcopy(self)
        euler = [x]
        z = y
        graph_edges = graph.get_edges()

        while len(graph_edges) > 0:
            u = None
            for node in euler:
                if graph.kaZu_grad(node) > 0:
                    u = node
                    z = u
                    break
            if not u:
                exit("DAAAAANGER or not??????")

            #print("Target-{}".format(z)) # debug
            sub_euler = []
            while True:
                #print("Current-{} Neighbours-{}".format(u, graph.get_neighbours(u))) # debug
                v, edge = graph.kaZu_next_edge(u, graph_edges)

                #print("e({}, {})".format(edge[0], edge[1])) # debug
                sub_euler.append(v)
                graph_edges.remove(edge)
                graph.remove_edge(edge[0], edge[1])
                u = v

                if u == z:
                    break

            #append sub list to list at a specific point
            for i, sub_node in enumerate(sub_euler):
                euler.insert(euler.index(u) + 1 + i, sub_node)
        return euler

    # ----------------------------------------------------------------
    # maybe not needed - after call a toGraph call is needed

    def add_node(self, node, edges=None):
        if not isinstance(edges, list):
            print("IllegalArgument: edges has to be a list")
            edges = []
        if node not in self.adjazenz.keys():
            self.adjazenz[node] = edges
            return self.adjazenz[node]
        else:
            print("Node {} already exists: no changes made", node)
            return self.get_neighbours_plus(node)

    def add_edge(self, node, edge: Edge):
        edges = self.adjazenz[str(node)]
        if edges is None:
            print("Node not found")
        else:
            assert isinstance(edges, list)
            if not self.allow_multi:
                if edge in edges:
                    print("Multi edges not allowed")
                    return
            edges.append(edge)

    def add_edges(self, node, edges: List[Edge]):
        for edge in edges:
            self.add_edge(node, edge)

    def remove_edge(self, node, edge):
        x, y = node, edge
        #print("({}, {})".format(x, y)) # debug
        if y not in self.adjazenz[x] and x not in self.adjazenz[y]:
            print("Edge {} in both directions not exists".format((x, y)))
            return
        if y not in self.adjazenz[x]:
            tmp = x
            x = y
            y = tmp
        self.adjazenz[x].remove(y)

    def remove_node(self, node):
        if self.adjazenz.pop(node, False):
            for n in self.adjazenz.keys():
                self.remove_edge(n, node)
