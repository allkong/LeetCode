class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cow = 0
        for i in range(len(secret)):
            bull += int(secret[i]==guess[i])
        for c in set(secret):
            cow += min(secret.count(c), guess.count(c))
        return f"{bull}A{cow-bull}B"