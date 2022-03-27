class Solution:
    def countPoints(self, rings: str) -> int:
        res = [''] * 10
        cnt = 0
        for i in range(0, len(rings), 2):
            res[int(rings[i+1])] += rings[i]
        for r in res:
            if 'R' in r and 'G' in r and 'B' in r:
                cnt += 1
        return cnt
            