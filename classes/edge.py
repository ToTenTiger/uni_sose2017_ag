class Edge:
    def __init__(self, node="", weight=0):
        self.node = node
        self.weight = weight

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            # full equality test with following:
            # return self.__dict__ == other.__dict__
            return self.node == other.node
        elif isinstance(other, str):
            return self.node == other
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        # remove function if class have mutable objects
        return hash(self.node)

    def __str__(self):
        #return "Edge[{}]".format(str(self.node))
        return str(self.node)

    def __repr__(self):
        #return "Edge[{}]".format(str(self.node))
        return str(self.node)

    def __unicode__(self):
        #return u"Edge[{}]".format(str(self.node))
        return u""+str(self.node)
