class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1

        while l < r:
            mid = (l + r) // 2
            pivot_element = matrix[mid // n][mid % n] #将mid索引映射为矩阵中的元素

            if pivot_element < target:
                l = mid + 1
            else:
                r = mid 
        return True if matrix[r // n][r % n ] == target else False


