from itertools import groupby
from heapq import *
from typing import Iterable


class Node:
    def __init__(self,
                 left_child=None,
                 right_child=None,
                 mother=None,
                 value=None,
                 weight=None):
        self.left_child = left_child
        self.right_child = right_child
        self.mother = mother
        self.value = value
        self.weight = weight

    def set_children(self, left, right):
        self.left_child = left
        self.right_child = right

    def get_weight(self, result=None):
        if self.left_child is not None:
            result += self.left_child.get_weight()
        if self.right_child is not None:
            result += self.right_child.get_weight()
        return result + self.weight

    def __repr__(self):
        return "%s - %s — %s _ %s" % (self.item, self.weight, self.left, self.right)

    def __lt__(self, other):
        return self.weight < other.weight

    def __eq__(self, other):
        return self.weight == other.weight
