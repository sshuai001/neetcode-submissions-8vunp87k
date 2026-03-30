class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        less_num, more_num = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(less_num) > len(more_num):
            less_num, more_num = more_num, less_num
        
        l, r = 0, len(less_num) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            less_num_left = less_num[i] if i >= 0 else float("-infinity")
            less_num_right = less_num[i + 1] if i + 1 < len(less_num) else float("infinity")
            more_num_left = more_num[j] if j >= 0 else float("-infinity")
            more_num_right = more_num[j + 1] if j + 1 < len(more_num) else float("infinity")

            if less_num_left <= more_num_right and more_num_left <= less_num_right:
                if total % 2:
                    return min(less_num_right, more_num_right)
                else:
                    return (max(less_num_left, more_num_left) + min(less_num_right, more_num_right)) / 2
            elif less_num_left > more_num_left:
                r = i - 1   
            else:
                l = i + 1

