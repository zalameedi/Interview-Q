class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums)-1, 2):
            freq = nums[i]
            val = nums[i+1]
            result.extend([val for i in range(freq)])
        return result
            