class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        res = []
        c1, c2 = ord(s[0]), ord(s[-2])
        r1, r2 = int(s[1]), int(s[-1])
        for i in range(c1, c2+1):
            for j in range(r1, r2+1):
                res.append(chr(i) + str(j))
        return res