class graph_partition:
    def __init__(self, proc_id: int, num_procs: int):
        self.proc_id = proc_id
        self.num_procs = num_procs
        self.current = -1

    def fit(self, num_vertices):
        self.num_vertices = num_vertices
        sum_vertices = sum(i for i in range(self.num_vertices))
        div, mod = divmod(sum_vertices, self.num_procs)
        self.procs = [div] * self.num_procs
        for i in range(mod):
            self.procs[i] += 1

        sum_procs = sum(self.procs[:self.proc_id])
        num = self.num_vertices - 2
        for i in range(0, self.num_vertices-1):
            if sum_procs - 1 <= num:
                self.first, self.second = i, self.num_vertices - 1 - num + sum_procs - 1
                break
            else:
                num += self.num_vertices - 2 - i
        return self

    def __iter__(self):
        return self

    def __len__(self):
        return self.procs[self.proc_id]

    def __next__(self):
        self.current += 1
        if self.current >= self.procs[self.proc_id]:
            raise StopIteration
        current = self.second + 1
        if current < self.num_vertices:
            self.second = current
        else:
            self.first, self.second = self.first + 1, self.first + 2
        return (self.first, self.second)
