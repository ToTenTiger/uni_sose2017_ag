class FoundCircleError(Exception):
    """Exception raised if circles in a graph are found and not allowed"""
    pass


class MultiEdgesNotAllowedError(Exception):
    """Exception raised if there was a try to add an already existing edge when not allowed"""
    pass
