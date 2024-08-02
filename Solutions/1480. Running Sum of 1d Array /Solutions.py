#https://leetcode.com/problems/running-sum-of-1d-array/

# Difficulty: Easy

# tags: prefix/postfix, range query

# Time complexity : O(n) Space Complexity: O(n)


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        prefix_arr = []

        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            prefix_arr.append(prefix_sum)
        return prefix_arr

