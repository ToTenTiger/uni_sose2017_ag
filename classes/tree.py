from .node import Node


class Tree:
    def __init__(self, root: Node):
        self.root = root
        self.nnk = "0"
        self.depth = 1

    def add_node(self, node):
        if not self.root.has_child():
            self.root = node
        else:
            self.find_value()

    def find_value(self, current_node=None, value=None):
        result = False
        if current_node is not None:
            nd = current_node
        else:
            nd = self.root

        if nd.has_child():
            if nd.left_child is not None:
                self.find_value(nd.left_child, value)
            if result:
                self.find_value(nd.right_child, value)

    def delete_node(self, node):
        pass
