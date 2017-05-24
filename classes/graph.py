from copy import deepcopy
from re import compile as regex_compile
from typing import List

import graphviz as gv
from graphviz.dot import Dot

import global_vars
from .errors import MultiEdgesNotAllowedError
from .edge import Edge


class Graph:
    def __init__(self,
                 title=None,
                 filename: str="graph",
                 body=None,
                 adjazenzdict: dict=None,
                 allow_multi=False,
                 weighted=False,
                 value=None,
                 onfly_allowed=True,
                 graph_attr=None,
                 node_attr=None,
                 edge_attr=None):
        self.dot = Dot()

        self.title = title
        self.filename = filename if filename.endswith(".gv") else filename + ".gv"
        self.body = body
        self.adjazenz = adjazenzdict if adjazenzdict else dict()
        self.allow_multi = allow_multi
        self.weighted = weighted
        if not adjazenzdict and value:
            self.read_input(value, onfly_allowed)
        self.graph_attr = graph_attr if graph_attr else {}
        self.node_attr = node_attr if node_attr else {}
        self.edge_attr = edge_attr if edge_attr else {}

    def read_input(self, value=None, onfly_allowed=True):
        self.clear()
        raw_input = value
        if onfly_allowed and global_vars.onflygraph:
            formats = dict(default="(<node>: <list of <node>>;)*;",
                           weighted="(<node>: <list of <node>-<weight>>;)*;")
            regex_format = formats["default"] if not self.weighted else formats["weighted"]

            print("\nPassed adjazenz list for {}: {}".format(self.filename, value))
            print("Please use following string format:\n" +
                  " |- <node>\t   = [A-Za-z0-9_]\n" +
                  " |- <adjazenzlist> = {}".format(regex_format))
            new_input = input("Enter another <adjazenzlist> or just press [Enter]: ")
            if new_input:
                raw_input = new_input

        if not self.weighted:
            pattern = regex_compile("(\w+):(\w+|[\w,]*);")
            for (node, edges) in pattern.findall(raw_input):
                edge_list = str(edges).split(",")
                n = Edge(node)
                self.add_node(n, [])
                # converts list<str> on the fly to list<Edge>
                # list+filter contruct to ignor empty entries
                self.add_edges(n, [Edge(e) for e in list(filter(None, edge_list))])
        else:
            pattern_nodes = regex_compile("(\w+):(|(?:\w+-\d+(?:\.\d+)?)(?:,\w+-\d+(?:\.\d+)?)*);")
            pattern_edges = regex_compile("(\d+)-(\d+(?:\.\d+)?)")
            for (node, edges) in pattern_nodes.findall(raw_input):
                n = Edge(node)
                self.add_node(n, [])
                for (edge, weight) in pattern_edges.findall(edges):
                    e = Edge(edge, weight)
                    self.add_edge(n, e)

    def to_dot(self):
        self.dot = gv.Graph(
            name=self.title,
            directory="graphs",
            filename=self.filename,
            strict=not self.allow_multi,
            graph_attr=self.graph_attr,
            node_attr=self.node_attr,
            edge_attr=self.edge_attr,
            body=self.body
        )

        if not self.body:
            self._buildDot()
        return self.dot

    def to_string(self):
        ag = ""
        for node in self.get_nodes():
            ag += "{}:".format(node)
            neighbours_plus = self.get_neighbours_plus(node)
            for i, edge in enumerate(neighbours_plus):
                ag += "{}".format(edge)
                if self.weighted:
                    ag += "-{}".format(edge.weight)
                if i < len(neighbours_plus)-1:
                    ag += ","
            ag += ";"
        ag += ";"
        return str(ag)

    def __str__(self):
        return self.to_string()

    def __repr__(self):
        return self.__str__()

    # ----------------------------------------------------------------
    # helper methods

    def clear(self):
        self.adjazenz.clear()

    def get_neighbours_plus(self, node):
        return list(map(
            lambda e: deepcopy(e),
            self.adjazenz.get(str(node)) or []
        ))

    def get_neighbours_minus(self, node):
        predecessors = []
        for n, es in self.adjazenz.items():
            for e in es:
                if e == str(node):
                    predecessors.append(Edge(n, e.weight))
        return predecessors

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
            color = str(node.color) if node.color else None
            self.dot.node(node.name, fillcolor=color)
            for edge in edges:
                label = str(edge.weight) if self.weighted else None
                color = str(edge.color) if edge.color else None
                self.dot.edge(node.name, edge.name, label, fillcolor=color)

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
            print("[INFO] Method hierholzer not supported for graphs without cycles")
            return

        d = []  # liste von allen eckengraden
        ung = []  # liste von ecken mit ungeradem grad
        for node in self.adjazenz.keys():
            grad = self.grad(node)
            d.append(grad)
            if grad % 2 == 1:
                ung.append(node)

        if 0 in d:
            print("[INFO] Kein Euler-KaZu, der Graph ist nicht zh")
            return False
        if len(ung) > 2 or len(ung) == 1:
            print("[INFO] Kein Euler-KaZu, > 2 oder 1 Ecke(n) mit ung. Grad")
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

            #print("[DEBUG] Target-{}".format(z)) # debug
            sub_euler = []
            while True:
                #print("[DEBUG] Current-{} Neighbours-{}".format(u, graph.get_neighbours(u))) # debug
                v, edge = graph.kaZu_next_edge(u, graph_edges)

                #print("[DEBUG] e({}, {})".format(edge[0], edge[1])) # debug
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

    def colorize(self, c_max):
        result = "</>", "</>"

        coloring = dict()
        for n in self.get_nodes():
            coloring[n] = 0

        colors = list(range(1, c_max+1))

        # expecting first node is a root
        if not self.colorize_find(colors, coloring, self.get_nodes()[0]):
            return result

        for node in self.adjazenz.keys():
            node.color = coloring[node]

        result = len(set(list(coloring.values()))), list(coloring.values())
        return result

    def colorize_find(self, colors, coloring, current_node):
        neighbours = list(set(self.get_neighbours(current_node)))

        # find available colors
        unused_colors = colors[:]
        for neighbour in neighbours:
            if coloring[neighbour] in unused_colors:
                unused_colors.remove(coloring[neighbour])

        while unused_colors:

            # use smallest available color (because maybe not all colors needed)
            coloring[current_node] = min(unused_colors)

            # all nodes have a color
            if not 0 in list(coloring.values()):
                return True

            uncolored_neighbours = []
            for neighbour in neighbours:
                if coloring[neighbour] == 0:
                    uncolored_neighbours.append(neighbour)

            if uncolored_neighbours:
                # depth-first coloring
                for neighbour in uncolored_neighbours:
                    result = self.colorize_find(colors, coloring, neighbour)
                    if result:
                        return True
                    elif result is None:
                        pass  # all neighbours already colored
                    elif not result:
                        coloring[current_node] = 0
                        unused_colors.remove(min(unused_colors))
                        break
            else:
                return None

        # all colors were used by neighbours or as unsuccessful solution
        return False

    # ----------------------------------------------------------------
    # maybe not needed - after call a toGraph call is needed

    def add_node(self, node, edges=None):
        if not isinstance(edges, list):
            print("[ERROR] IllegalArgument: edges has to be a list")
            edges = []
        if node not in self.adjazenz.keys():
            self.adjazenz[node] = edges
            return self.adjazenz[node]
        else:
            print("[DEBUG] Node {} already exists: no changes made", node)
            return self.get_neighbours_plus(node)

    def add_edge(self, node, edge: Edge):
        edges = self.adjazenz[str(node)]
        if edges is None:
            print("[DEBUG] Node not found")
        else:
            assert isinstance(edges, list)
            if not self.allow_multi and edge in edges:
                raise MultiEdgesNotAllowedError
            self.adjazenz[str(node)].append(edge)

    def add_edges(self, node, edges: List[Edge]):
        for edge in edges:
            self.add_edge(node, edge)

    def remove_edge(self, node, edge):
        x, y = node, edge
        #print("[DEBUG] ({}, {})".format(x, y)) # debug
        if y not in self.adjazenz[x] and x not in self.adjazenz[y]:
            print("[DEBUG] Edge {} in both directions not exists".format((x, y)))
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
