class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # youtube solution
        n = len(citations)

        paper_counts = [0] * (n+1)

        for c in citations:
            # we do the min just in case it goes overbound
            paper_counts[min(n,c)] += 1

        # set the h to the highest possible
        h = n
        papers = paper_counts[n]

        # go the lowest possible
        while papers < h:
            h -= 1
            papers += paper_counts[h]

        return h

