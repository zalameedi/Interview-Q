class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return self.fib(n-1)+self.fib(n-2)
            
            
    
    def fib2(self, n):
        result = 0
        while n > 1:
            result += (n-1) + (n-2)
            n -= 1
        return result
            