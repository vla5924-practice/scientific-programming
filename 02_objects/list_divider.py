class list_divider(list):
    def __init__(self, *args):
        super().__init__(*args)

    def __truediv__(self, n: int):
        if not isinstance(n, int):
            raise TypeError
        if n < 1:
            raise ValueError
        div, mod = divmod(len(self), n)
        parts = []
        for i in range(n):
            first = i * div + min(i, mod)
            last = (i + 1) * div + min(i + 1, mod)
            parts.append(self[first:last])
        return parts
