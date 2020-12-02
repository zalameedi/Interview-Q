class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum_d = 0
        result = 0
        for x in str(n):
            sum_d += int(x)
            product *= int(x)
        return product-sum_d
            