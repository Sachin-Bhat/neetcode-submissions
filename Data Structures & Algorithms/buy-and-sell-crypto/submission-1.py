class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Intution
        --------
        we need 2 variables to track profit and max_profit

        Let us look at edge cases or early exit conditions
        1. prices are empty -> return 0
        2. prices are in descending order -> 0

        sliding window approach here
        update conditions
        if prices[l] > prices[r] -> increment l to r
        else -> take profit if greater than max_profit update it
        while l >= r -> increment r this anyway happens
        '''
        profit, max_profit = 0, 0
        L = 0

        if len(prices) == 0 or prices == sorted(prices)[::-1]:
            return 0

        for R in range(1, len(prices)):
            if prices[L] > prices[R]:
                L = R
            else:
                profit = prices[R] - prices[L]
                if profit > max_profit:
                    max_profit = profit
        return max_profit
