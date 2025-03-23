class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        # my attempt it is wrong

        # hashmap = {} # ind: val

        # for i,v in enumerate(nums):
        #     diff = target - hashmap[i]

        #     if diff in hashmap.values:
        #         return [nums[i], diff]
        #     hashmap[i] = v

        hash_map = {} # val: indx

        for i,v in enumerate(nums):
            diff = target - v

            if diff in hash_map:
                return [i, hash_map[diff]]
            hash_map[v] = i
