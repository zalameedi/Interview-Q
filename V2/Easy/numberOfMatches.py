class Solution:
    def numberOfMatches(self, n: int) -> int:
        result = []
        while n > 1:
            if n % 2 == 0:
                n = n/2
                result.append(n)
            else:
                n = (n-1)/2
                result.append(int(n))
                n += 1
        return int(sum(result))