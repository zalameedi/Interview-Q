class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.Stack = []
        
        
    def push(self, x: int) -> None:
        if len(self.Stack) != self.maxSize:
            self.Stack.append(x)
        else:
            return None
        
    def pop(self) -> int:
        if len(self.Stack) == 0:
            return -1
        else:
            x = self.Stack.pop()
            return x
        

    def increment(self, k: int, val: int) -> None:
        if (len(self.Stack) < k):
            for x in range(0, len(self.Stack)):
                self.Stack[x] += val
        else:
            for x in range(0, k):
                self.Stack[x] += val
        
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)