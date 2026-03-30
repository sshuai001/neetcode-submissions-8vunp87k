class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque() #index
        l = r = 0
        
        for r in range(len(nums)):
            #pop smaller values from q
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            #remove left value from window
            if q[0] < l:
                q.popleft()

            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
        return res

        