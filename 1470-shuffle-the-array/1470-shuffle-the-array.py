class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x=[]
        for i in range(n):
            x.append(nums[i])
            x.append(nums[i+n])
        return x