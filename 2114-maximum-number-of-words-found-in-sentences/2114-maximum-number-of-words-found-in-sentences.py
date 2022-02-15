class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for i in range(len(sentences)):
            sentence = sentences[i]
            s = sentence.split()
            if ans < len(s):
                ans = len(s)
        return ans