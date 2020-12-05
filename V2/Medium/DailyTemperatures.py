class Solution:
    def dailyTemperatures(self, T):
        ans = [0]*len(T)
        stack = []
        for i in range(len(T)): 
            while stack and T[stack[-1]] < T[i]: 
                ii = stack.pop()
                ans[ii] = i - ii 
            stack.append(i)
        return ans 

            



sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))


# class Solution:
#     def dailyTemperatures(self, T):
#         awaited_days = []
#         for i in range(0,len(T)):
#             result = 0
#             if ((i+1 < len(T)) and (T[i] < T[i+1])):
#                 awaited_days.append(1)
#             else:
#                 result = self.dailyTemperaturesHelper(T[i], T[i::])
#                 awaited_days.append(result)
#         return awaited_days
    
#     def dailyTemperaturesHelper(self, temp, T):
#         for i in range(0, len(T)):
#             if temp < T[i]:
#                 return i
#         return 0