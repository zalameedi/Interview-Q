class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for x in nums:
            if len(str(x)) % 2 == 0:
                result += 1
        return result
        