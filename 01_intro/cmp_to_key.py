def cmp_to_key(comparator):
    class Proxy:
        def __init__(self, obj):
            self.obj = obj

        def __gt__(self, other):
            return comparator(self.obj, other.obj) > 0
    return Proxy
