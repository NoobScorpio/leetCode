from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # return max(sum(account) for account in accounts)
        wealth = []
        for i in accounts:
            w = 0
            for j in i:
                w += j
            wealth.append(w)
        return max(wealth)
    
