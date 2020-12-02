class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = 0
        ls = []
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if nums[i] > nums[j] and (i != j):
                    result += 1
            ls.append(result)
            result = 0
        return ls