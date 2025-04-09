class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {} # val: idx

        for i,v in enumerate(nums):
            diff = target - v

            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[v] = i

        # time complexity: O(n)
        # space complexity: O(n)
