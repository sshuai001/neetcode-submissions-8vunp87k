class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0
        l_max, r_max = height[left], height[right]

        while left < right:
            if l_max < r_max:
                left += 1
                l_max = max(l_max, height[left])
                res += l_max - height[left]
            else:
                right -= 1
                r_max = max(r_max, height[right])
                res += r_max - height[right]
        return res