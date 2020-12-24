class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr = sorted(arr)
        for a in reversed(arr):
            if a == arr.count(a):
                return a
        return -1