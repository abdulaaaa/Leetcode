class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # add the nums to a hashmap with their index:
        # ex: [2:0, 7: 1, 11: 2, 15: 3]
        # this must be done through a loop of the nums
        # find the difference between the target and current num
        # if it is located in hash map return the num and hashmap[diff]
        # else add it to the hash_map

        hash_map = {} # val: idx

        for i,v in enumerate(nums):
            diff = target - v
            if diff in hash_map:
                return [i, hash_map[diff]]
            hash_map[v] = i
