class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        for i in candies:
            i += extraCandies
            if i >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return result