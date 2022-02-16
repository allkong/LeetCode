class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]
        for candy in candies:
            candy+=extraCandies
            ans.append(bool(candy>=max(candies)))
        return ans