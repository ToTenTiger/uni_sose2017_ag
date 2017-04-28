class Request():

    def __init__(self, interval_start=None, interval_end=None):
        self.interval_start = interval_start
        self.interval_end = interval_end
        self.interval_lenght = interval_end - interval_start

    def compatible(self, other):
        if not isinstance(other, Request):
            return
        return other.interval_start <= self.interval_end and other.interval_end < self.interval_start

    def is_start_earlier(self, other):
        if not isinstance(other, Request):
            return
        return self.interval_start < other.interval_start

    def is_end_earlier(self, other):
        if not isinstance(other, Request):
            return
        return self.interval_end < other.interval_end

    def is_shorter(self, other):
        if not isinstance(other, Request):
            return
        return self.interval_lenght < other.interval_lenght

    def __repr__(self):
        return "({}-{})".format(self.interval_start, self.interval_end)
