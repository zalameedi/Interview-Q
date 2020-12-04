class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        j = 0
        for i in index:
            result.insert(i, nums[j])
            j += 1
        return result