class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        else:
            return self.fib(n-1)+self.fib(n-2)
            
            
    
    def fib2(self, n):
        result = 0
        while n > 1:
            result += (n-1) + (n-2)
            n -= 1
        return result
            