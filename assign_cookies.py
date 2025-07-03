class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        i, j = 0, 0
        g.sort()
        s.sort()
        total = 0
        while j < len(s) and i < len(g):
            if s[j] >= g[i]:
                total += 1
                i += 1
                j += 1
            else:
                j += 1
        return total