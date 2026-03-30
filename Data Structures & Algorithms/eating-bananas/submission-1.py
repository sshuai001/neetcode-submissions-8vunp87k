class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = l
        while l <= r:
            mid = (l + r) // 2
            total_time = 0

            for pile in piles:
                total_time += math.ceil(pile / mid)
            # 速度够快（或者刚好），记录这个结果，并尝试更慢的速度
            if total_time <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res 
    
                