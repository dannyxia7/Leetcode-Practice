class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #pair, (index, value)

        for index, i in enumerate(temperatures):
            while stack and i > stack[-1][1]:
                stackI, stackT = stack.pop()
                res[stackI] = index - stackI 
            stack.append([index, i])
    
        return res