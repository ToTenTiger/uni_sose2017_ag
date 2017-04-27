class Node:
    def __init__(self,
                 left_child=None,
                 right_child=None,
                 mother=None,
                 value=None):
        self.left_child = left_child
        self.right_child = right_child
        self.mother = mother
        self.value = value
        self.weight = self.get_and_update_weight_recursive()

    def set_children(self, left=None, right=None):
        if self.right_child != right and self.left_child != left:
            self.left_child = left
            self.right_child = right
            self.get_and_update_weight_recursive()

    def get_and_update_weight_recursive(self):
        left = 0
        right = 0

        if self.left_child is not None and self.right_child is not None:
            if self.left_child is not None:
                left = self.left_child.get_and_update_weight_recursive()
            if self.right_child is not None:
                right = self.right_child.get_and_update_weight_recursive()
            self.weight = left + right

        return self.weight

    def manipulate_weight(self, value):
        self.weight += value
        if self.mother is not None:
            self.get_and_update_weight_recursive()

    def is_valide(self):
        result = True

        if self.right_child is not None:
            result = self.right_child.is_valide()
        if self.left_child is not None:
            result = self.left_child.is_valide()

        return result

    def __repr__(self):
        return "%s - %s — %s _ %s" % (self.value, self.weight, self.left_child, self.right_child)

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __eq__(self, other):
        return self.weight == other.weight
