class Solution:
    def minSteps(self, s: str, t: str) -> int:
        for c in s:
            if c in t:
                s = s.replace(c, '', 1)
                t = t.replace(c, '', 1)
        return len(t)