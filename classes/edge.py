class Edge:
    def __init__(self, name="", weight=0, color=None):
        self.name = name
        self.weight = weight
        self.color = color

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            # full equality test with following:
            # return self.__dict__ == other.__dict__
            return self.name == other.name
        elif isinstance(other, str):
            return self.name == other
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        # remove function if class have mutable objects
        return hash(self.name)

    def __str__(self):
        #return "Edge[{}]".format(str(self.name))
        return str(self.name)

    def __repr__(self):
        #return "Edge[{}]".format(str(self.name))
        return str(self.name)

    def __unicode__(self):
        #return u"Edge[{}]".format(str(self.name))
        return u""+str(self.name)
