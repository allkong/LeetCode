class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i in range(start, n * 2 + start, 2):
            ans ^= i
        return ans