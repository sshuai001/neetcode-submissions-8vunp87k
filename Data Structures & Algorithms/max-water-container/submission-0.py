class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_capacity = 0
        while left < right:
            curr_capacity = (right - left) * min(heights[left],heights[right])
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            max_capacity = max(max_capacity,curr_capacity)
        return max_capacity
        
            