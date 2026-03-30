class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        heights.insert(0,0)
        max_area = 0
        for i, item in enumerate(heights):
            while stack and heights[i] < heights[stack[-1]]:
                right = i
                curr = stack.pop()
                left = stack[-1]

                height = heights[curr]
                width = right - left - 1
                max_area = max(max_area, (height * width))
            stack.append(i)
        return max_area


