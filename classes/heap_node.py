class HeapNode:

    def __init__(self, value=None, weight=0):
        self.value = value
        self.weight = weight
        self.left = None
        self.right = None

    def set_childs(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return "{}:{} | {} - {}"\
            .format(self.value, self.weight, self.left, self.right)

    def __lt__(self, other):
        return self.weight > other.weight

    def __gt__(self, other):
        return self.weight < other.weight

    def __eq__(self, other):
        return self.weight == other.weight

