class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        sorted_nums = sorted(nums)

        hash_map = {}

        ret = []

        for i,v in enumerate(sorted_nums):
            if v not in hash_map:
                hash_map[v] = i

        for i in nums:
            ret.append(hash_map[i])
        return ret

