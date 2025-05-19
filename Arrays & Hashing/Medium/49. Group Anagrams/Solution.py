class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # I needed help from neetcode on how to solve this, I have an idea but this question was too complex for me

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)

        return list(res.values())
