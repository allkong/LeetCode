class Solution:
    def minimumSum(self, num: int) -> int:
        nums=list(str(num))
        ans=[]
        for i in range(len(nums)):
            nums[i]=int(nums[i])
        for i in range(2):
            ans.append(min(nums)*10)
            nums.remove(min(nums))
        ans+=nums
        return sum(ans)