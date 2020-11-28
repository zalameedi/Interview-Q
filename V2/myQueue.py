class MyQueue:

    def __init__(self):
        self.queue = []
        
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        

    def pop(self) -> int:
        if (not self.empty()):
            x = self.queue[0]
            del self.queue[0]
            return x
        else:
            return
        

    def peek(self) -> int:
        if (not self.empty()):
            x = self.queue[0]
            return x
        else:
            return
        

    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()