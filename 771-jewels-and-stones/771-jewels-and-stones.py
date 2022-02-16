class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        for jewel in jewels:
            ans += stones.count(jewel)
        return ans