class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        str = ""
        while columnNumber > 0:
            columnNumber -= 1
            str += chr(columnNumber % 26 + 65)
            columnNumber //= 26
        return str[::-1]