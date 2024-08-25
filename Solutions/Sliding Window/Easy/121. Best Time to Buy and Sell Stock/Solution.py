# 121. Best Time to Buy and Sell Stock (Medium)

# Topics: Array, Dynamic Programming

# Question: You are given an array prices where prices[i] is the price of a
# given stock on the ith day. You want to maximize your profit by choosing a
# single day to buy one stock and choosing a different day in the future to
# sell that stock. Return the maximum profit you can achieve from this
# transaction. If you cannot achieve any profit, return 0.

# Time Complexity: O(n) - We are searching the list forward in
# linear fashion

# Space Complexity: O(1) - no extra data structure is being used to store values

# Time Spent: 00:12:17

# My Solution:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0
        max_value = 0

        for right in range(1,len(prices)):
            dif = prices[right] - prices[left]

            if dif < 0:
                left = right
            else:
                max_value = max(max_value, dif)

        return max_value


# Time Complexity: O(n) - (Same as above)

# Space Complexity: O(1) - (Same as above)

# NeetCode Solution:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP