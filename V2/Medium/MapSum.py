class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.MapSum = {}
        

    def insert(self, key: str, val: int) -> None:
        self.MapSum[key] = val
        

    def sum(self, prefix: str) -> int:
        result = 0
        prefix_length = ""
        for k in self.MapSum:
            prefix_length = k[0:len(prefix)]
            if (prefix == prefix_length):
                result += self.MapSum[k]
        return result
        
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)