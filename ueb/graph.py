import graphviz as gv
from re import compile as regex_compile
from graphviz.dot import Dot
from copy import deepcopy


class Graph:
    def __init__(self, title=None, filename=None, adjazenzlist=None):
        self.dot = None
        self.title = title
        assert isinstance(filename, str)
        self.filename = filename if filename.endswith(".gv") else filename + ".gv"
        self.adjazenz = dict()
        if isinstance(adjazenzlist, dict):
            self.adjazenz = adjazenzlist

    def read_input(self, value=None, text="Insert graph input string :> "):
        self.clear()
        raw_input = value or input(text)
        pattern = regex_compile("(\w+):(\w+|[\w,]*);")
        for (node, edges) in pattern.findall(raw_input):
            edge_list = str(edges).split(",")
            # list+filter contruct to ignor empty entries
            self.adjazenz[node] = list(filter(None, edge_list))

    def to_graph(self, allow_multi=True):
        self.dot = gv.Graph(
            name=self.title,
            directory="graphs",
            filename=self.filename,
            strict=not allow_multi,
            graph_attr={},
            node_attr={},
            edge_attr={}
        )
        self.__buildDot()
        return self.dot

    # ----------------------------------------------------------------
    # helper methods

    def clear(self):
        self.adjazenz.clear()

    def get_neighbours_plus(self, node):
        # print("{} {}".format(node, self.adjazenz.get(str(node))))
        return self.adjazenz.get(str(node)) or []

    def get_neighbours_minus(self, node):
        neighbours = []
        for (n, e) in self.adjazenz.items():
            if node in e:
                neighbours.append(n)
        return neighbours

    def get_neighbours(self, node):
        return self.get_neighbours_plus(node) + self.get_neighbours_minus(node)

    def get_edges(self):
        K = []
        for node in self.adjazenz.keys():
            for edge in self.get_neighbours_plus(node):
                K.append((node, edge))
        return K

    # ----------------------------------------------------------------
    # 'private' methods

    def __buildDot(self):
        for node, edges in self.adjazenz.items():
            self.dot.node(node)
            for edge in edges:
                self.dot.edge(node, edge)

    # ----------------------------------------------------------------
    # excise methods

    def bnb(self, x, y):
        return y in self.get_neighbours_plus(x) or x in self.get_neighbours_plus(y)

    def aus_grad(self, x):
        return len(self.get_neighbours_plus(x))

    def ein_grad(self, x):
        ein_grad = 0
        for (node, edges) in self.adjazenz.items():
            if x in edges:
                ein_grad += 1
        return ein_grad

    def grad(self, x):
        return self.aus_grad(x) + self.ein_grad(x)

    def hierholzer(self):
        assert isinstance(self.dot, Dot)
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

        u = None
        ziel = next(iter(self.adjazenz.keys()))  # beliebige ecke -> derzeit erste TODO wofür?
        if len(ung) == 0:
            u = next(iter(self.adjazenz.keys()))  # TODO could be the same as ziel already
        elif len(ung) == 2:
            u, ziel = ung
        else:
            print("Kein Euler-KaZu, > 2 oder 1 Ecke(n) mit ung. Grad")
            return u

        return self.kaZu(u, ziel)

    def kaZu(self, x, y):
        old_adjazenz = deepcopy(self.adjazenz)
        try:
            euler = [x]
            z = y
            K = self.get_edges()
            while len(K) > 0:
                u = None
                for node in euler:
                    if self.grad(node) > 0:
                        u = node
                        break
                while True:
                    #print("node u {} and neigbhours {} first entry v {}".format(u, self.getNeighbours(u), self.getNeighbours(u)[0]))
                    v = self.get_neighbours(u)[0]
                    euler.append(v)
                    edge = (u, v)
                    if K.count(edge) <= 0:
                        edge = (v, u)
                    print("count of {}: {} in K {} ".format(edge, K.count(edge), K))
                    K.remove(edge)
                    self.remove_edge(edge)

                    if u == z:
                        break
            return euler
        finally:
            self.adjazenz = old_adjazenz

    # ----------------------------------------------------------------
    # maybe not needed - after call a toGraph call is needed

    def add_node(self, node, edges=None):
        if not isinstance(edges, list):
            if edges is not None:
                print("IllegalArgument: edges has to be a list")
            edges = []
        if node not in self.adjazenz.keys():
            return self.adjazenz.get(node, edges)
        else:
            print("Node {} already exists: no changes made", node)
            return self.get_neighbours_plus(node)

    def add_edge(self, node, edge):
        edges = self.get_neighbours_plus(node)
        if edges is None:
            print("Node not found")
        else:
            assert isinstance(edges, list)
            edges.append(edge)

    def remove_edge(self, edge):
        x, y = edge
        edges = self.get_neighbours_plus(x)
        if y in edges:
            edges.remove(edge)

    def remove_node(self, node_to_delete):
        if self.adjazenz.pop(node_to_delete, False):
            for node in self.adjazenz.keys():
                self.remove_edge((node, node_to_delete))