class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque() #index
        l = 0

        for r in range(len(nums)):
            #如果当前元素比队尾元素大，队尾元素不可能成为最大值
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            # 如果左边界 l 已经超过了队首记录的索引 q[0]
            # 说明队列里最强大的那个值已经滑出窗口范围了
            if l > q[0]:
                q.popleft()
            #当右边界移动到形成窗口
            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
        return res
