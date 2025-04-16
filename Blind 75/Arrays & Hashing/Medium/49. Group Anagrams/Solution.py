class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # I needed help from neetcode on how to solve this, I have an idea but this question was too complex for me

        res = defaultdict(list)  # defaultdict lets you create automatic value for a key that doesn't exist yet.
        # in this scenario the key is a list

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1  # getting ascii value
            res[tuple(count)].append(s) # we used a tuple because the key cant be mutable
        return list(res.values())
