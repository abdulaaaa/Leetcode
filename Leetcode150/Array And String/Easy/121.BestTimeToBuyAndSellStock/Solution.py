class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # neetcode solution
        l,r = 0, 1 #left = buy. right = buy
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r # we found a new low
            r += 1
        return maxP
