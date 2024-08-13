# 49. Group Anagrams (Medium)

# Topics: Array, Hash Table, String, Sorting

# Question: Given an array of strings strs, group the anagrams together. You can
# return the answer in any order.

# Time Complexity: O(n logn) - this is a rough estimate the actual answer is way
# longer

# Space Complexity: O(n) - Stores key value pairs

# Time Spent: 00:23:20

# My Solution:
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        values = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in values:
                values[sorted_word] = []
            values[sorted_word].append(word)

        sorted_keys = sorted(values.keys())
        final_values = []
        for key in sorted_keys:
            final_values.append(values[key])

        return final_values



# Time Complexity: O(m * n) - m is the amount of word and n is amount of
# characters in each word

# Space Complexity: O(m * n) - m is the amount of word and n is amount of
# characters in each word

# NeetCode Solution:
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return res.values()
