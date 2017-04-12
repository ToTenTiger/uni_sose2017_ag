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

    def toGraph(self, allow_multi=True):
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

    def getNeighboursPlus(self, node):
        # print("{} {}".format(node, self.adjazenz.get(str(node))))
        return self.adjazenz.get(str(node)) or []

    def getNeighboursMinus(self, node):
        neighbours = []
        for (n, e) in self.adjazenz.items():
            if node in e:
                neighbours.append(n)
        return neighbours

    def getNeighbours(self, node):
        return self.getNeighboursPlus(node) + self.getNeighboursMinus(node)

    def getEdges(self):
        K = []
        for node in self.adjazenz.keys():
            for edge in self.getNeighboursPlus(node):
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
        return y in self.getNeighboursPlus(x) or x in self.getNeighboursPlus(y)

    def ausGrad(self, x):
        return len(self.getNeighboursPlus(x))

    def einGrad(self, x):
        einGrad = 0
        for (node, edges) in self.adjazenz.items():
            if x in edges:
                einGrad += 1
        return einGrad

    def grad(self, x):
        return self.ausGrad(x) + self.einGrad(x)

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
            K = self.getEdges()
            while len(K) > 0:
                u = None
                for node in euler:
                    if self.grad(node) > 0:
                        u = node
                        break
                while True:
                    # print("node u {} and neigbhours {} first entry v {}".format(u, self.getNeighbours(u), self.getNeighbours(u)[0]))
                    v = self.getNeighbours(u)[0]
                    euler.append(v)
                    print("K {} index {}".format(K, K.index((u, v))))
                    K.remove((u, v))
                    self.removeEdge(u, v)
                    if u == z:
                        break
            return euler
        finally:
            self.adjazenz = old_adjazenz

    # ----------------------------------------------------------------
    # maybe not needed - after call a toGraph call is needed

    def addNode(self, node, edges=None):
        if not isinstance(edges, list):
            if edges is not None:
                print("IllegalArgument: edges has to be a list")
            edges = []
        if node not in self.adjazenz.keys():
            return self.adjazenz.get(node, edges)
        else:
            print("Node {} already exists: no changes made", node)
            return self.getNeighboursPlus(node)

    def addEdge(self, node, edge):
        edges = self.getNeighboursPlus(node)
        if edges is None:
            print("Node not found")
        else:
            assert isinstance(edges, list)
            edges.append(edge)

    def removeEdge(self, node, edge):
        edges = self.getNeighboursPlus(node)
        if edge in edges:
            edges.remove(edge)

    def removeNode(self, node_to_delete):
        if self.adjazenz.pop(node_to_delete, False):
            for node in self.adjazenz.keys():
                self.removeEdge(node, node_to_delete)