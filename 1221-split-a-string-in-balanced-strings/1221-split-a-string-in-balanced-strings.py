class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt=0
        ans=0
        for c in s:
            if c=="R":
                cnt+=1
            elif c=="L":
                cnt-=1
            
            if cnt==0:
                ans+=1
        return ans