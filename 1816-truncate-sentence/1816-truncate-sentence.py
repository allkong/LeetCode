class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        sen = s.split()
        return ' '.join(sen[:k])