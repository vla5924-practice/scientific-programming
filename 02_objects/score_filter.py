class score_filter:
    def __init__(self, min_score, max_score):
        self.min_score = min_score
        self.max_score = max_score

    @staticmethod
    def superadd(lst):
        result = []
        total = 0
        for i in lst:
            total += i
            result.append(total)
        return result

    def fit(self, x, y, iterbl):
        x = self.superadd(x)
        y = self.superadd(y)
        def cond(i, j): return (x[i] * y[j]) / (x[len(x) - 1] * y[len(y) - 1])
        self.result = [(i, j) for i, j in iterbl
                       if self.min_score < cond(i, j) < self.max_score]

    def __iter__(self):
        return (i for i in self.result)
