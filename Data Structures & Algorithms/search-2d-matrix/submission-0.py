class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened = [item for row in matrix for item in row]
        l, r = 0, len(flattened) - 1
        while l < r:
            mid = l + (r - l) // 2
            if flattened[mid] < target:
                l = mid + 1
            else:
                r = mid
        return True if flattened[l] == target else False 