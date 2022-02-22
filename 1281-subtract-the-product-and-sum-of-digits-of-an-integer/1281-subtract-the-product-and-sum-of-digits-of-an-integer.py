class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = list(str(n))
        p=1
        s=0
        for i in range(len(nums)):
            p*=int(nums[i])
            s+=int(nums[i])
        return p-s