import collections


class Bucket(list):
    """
    list with size limitation
    >>> b = Bucket(2) # []
    >>> b.push(1) # [1]
    >>> b.push(2) # [1, 2]
    >>> b.push(3) # [2, 3]
    >>> b = Bucket([1, 2, 3]) # [1, 2, 3]
    >>> b.push(4) # [2, 3, 4]
    >>> b = Bucket([1, 2, 3], size=2) # [2, 3]
    """

    def __init__(self, size_or_iterable, size=None):
        if isinstance(size_or_iterable, collections.Iterable):
            super(Bucket, self).__init__(size_or_iterable)
            if size:
                self.size = size
            else:
                self.size = len(self)
            self.truncate()
        else:
            super(Bucket, self).__init__()
            self.size = size_or_iterable

    def push(self, p_object):
        self.append(p_object)
        self.truncate()

    def truncate(self):
        if len(self) > self.size:
            for i in range(len(self) - self.size):
                del self[0]
