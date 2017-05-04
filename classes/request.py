class Request():

    def __init__(self, interval_start=None, interval_end=None):
        self.interval_start = interval_start
        self.interval_end = interval_end
        self.interval_length = interval_end - interval_start
        self.conflicts = None

    def compatible(self, other):
        if not isinstance(other, Request):
            return
        return (other.interval_start <= self.interval_end and other.interval_end < self.interval_start) or \
               (self.interval_start <= other.interval_end and self.interval_end < other.interval_start)

    def __repr__(self):
        return "({}-{})".format(self.interval_start, self.interval_end)
