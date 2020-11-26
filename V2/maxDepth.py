class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        result = 0
        for x in list(s):
            if x == '(':
                stack.append(x)
                if result < len(stack):
                    result = len(stack)
            if x == ')':
                try:
                    stack.pop()
                except(...):
                    return
        return result
                    