class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, item in enumerate(temperatures):
            while stack and item > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] =  i -prev_index
            #栈中存放的是索引
            stack.append(i)
        return res

