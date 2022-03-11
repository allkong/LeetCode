class Solution:
    def sortSentence(self, s: str) -> str:
        ans = s.split()
        res = [0] * len(ans)
        for a in ans:
            res[int(a[-1])-1] = a[:-1]
        return ' '.join(res)
