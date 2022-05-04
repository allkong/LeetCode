class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        if len(set(s)) == len(set(t)):
            for i in range(len(s)):
                if t[i] not in dic:
                    dic[t[i]] = s[i]
                elif dic[t[i]] != s[i]:
                    return False
            return True
        return False
        