class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for account in accounts:
            wealth = sum(account)
            richest = max(wealth, richest)
        return richest