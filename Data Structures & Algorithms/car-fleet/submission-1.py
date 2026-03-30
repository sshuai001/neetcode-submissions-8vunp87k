class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [[p,s] for p, s in zip(position, speed)]
        # 按起始位置从大到小排序（从离终点最近的车开始处理）
        # 为什么？因为前车决定了后车是否会被堵住。后车跑得快也没用，只能跟在前车后面。
        for p, s in sorted(pair)[::-1]:
            time = (target - p) / s
            stack.append(time)
            #stack[-1]后车时间, stack[-2]前车时间
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() #栈中元素数量代表车队数量,相撞时合为一个车队
        return len(stack)
            
