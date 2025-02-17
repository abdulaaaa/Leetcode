class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {} #val, idx

        for idx, val in enumerate(nums):

            diff = target - val
            if diff in hashmap:
                return idx, hashmap[diff]
            hashmap[val] = idx
