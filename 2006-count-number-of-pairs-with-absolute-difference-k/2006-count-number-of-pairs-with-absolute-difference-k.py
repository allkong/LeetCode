class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]-nums[j] == k:
                    cnt += 1
        return cnt