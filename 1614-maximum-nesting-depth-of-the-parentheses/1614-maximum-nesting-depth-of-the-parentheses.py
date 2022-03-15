class Solution:
    def maxDepth(self, s: str) -> int:
        st = []
        ans = 0
        for c in s:
            if c == '(':
                st.append('(')
            elif c == ')':
                st.pop()
            ans = max(ans, len(st))
        return ans