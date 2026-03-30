class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        #按位置排序
        pair = [[p,s] for p, s in zip(position,speed)]

        for p, s in sorted(pair)[::-1]: #反向遍历
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack) 

