from .errors import FoundCircleError

from .di_graph import DiGraph
from .edge import Edge
from .graph import Graph

from .node import Node
from .heap_node import HeapNode
from .request import Request

__all__ = ["Edge", "Graph", "DiGraph", "Node", "HeapNode", "Request", "FoundCircleError"]


def returnObject(values: dict):
    obj = type('', (object,), values)()
    # obj = type('', (object,), **kwargs)()
    # obj = lambda **kwargs: type("Object", (), kwargs)()
    return obj
