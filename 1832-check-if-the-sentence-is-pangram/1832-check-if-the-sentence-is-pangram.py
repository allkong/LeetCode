class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        cnt = 0
        for i in range(97, 123):
            if chr(i) in sentence:
                cnt += 1
        return cnt == 26