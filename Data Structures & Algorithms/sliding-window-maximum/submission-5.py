class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque() #index
        #构建大小为k的窗口
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        res.append(nums[q[0]])
        #滑动窗口
        for r in range(k, len(nums)):
            #移除离开窗口的元素
            if q[0] == r - k:
                q.popleft()
            #加入新元素，同时保持单调性
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            #记录当前窗口最大值
            res.append(nums[q[0]])
        return res
        

        