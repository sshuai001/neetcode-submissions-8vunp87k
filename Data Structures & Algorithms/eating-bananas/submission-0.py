class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            total_time = sum((p + mid - 1) // mid for p in piles)
            
            if total_time <= h:
                high = mid
            else:
                low = mid + 1
        return low