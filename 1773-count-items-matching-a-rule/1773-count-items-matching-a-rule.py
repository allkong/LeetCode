class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        cnt = 0
        ruleKeys = {'type':0, 'color':1, 'name':2}
        for item in items:
            if item[ruleKeys[ruleKey]]==ruleValue:
                cnt += 1
        return cnt