class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt = len(words)
        for word in words:
            for w in set(word):
                if w not in allowed:
                    cnt -= 1
                    break
        return cnt
            