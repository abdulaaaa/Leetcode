#https://leetcode.com/problems/range-sum-query-immutable/

# Difficulty: Easy

# tags: prefix/postfix, range query

# Time complexity : O(n) Space Complexity: O(n)
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []

        total = 0

        for num in nums:
            total += num
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        right_sum = self.prefix[right]
        left_sum = 0
        if left > 0:
            left_sum = self.prefix[left - 1]
        return right_sum - left_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)