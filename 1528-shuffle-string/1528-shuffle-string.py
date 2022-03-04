class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res=""
        for i in range(len(indices)):
            res+=s[indices.index(i)]
        return res