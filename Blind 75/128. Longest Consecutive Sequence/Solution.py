class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # we can't sort it, it would be O(nlogn) then

        # I am using help from neetcode

        numSet = set(nums)
        longest = 0

        for n in numSet: # neetcode uses nums here but that exceeds time limit in some cases
            # start of the longest sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                    longest = max(length, longest)
        return longest

        # time complexity: O(n)
        # space complexity: O(n)

