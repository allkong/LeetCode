class OrderedStream:

    def __init__(self, n: int):
        self.data = [None] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.data[idKey - 1] = value
        res = []
        if (idKey - 1) == self.ptr:
            for i in range(self.ptr, len(self.data)):
                if self.data[self.ptr] is None:
                    break
                res.append(self.data[self.ptr])
                self.ptr += 1
        return res