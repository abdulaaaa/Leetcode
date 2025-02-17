class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # neetcode solution

        # this uses boyer moore's algorithm

        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res