class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            # 优化 1: 如果当前数字大于 0，后面三个数之和必然大于 0，直接结束
            if nums[i] > 0: break
            #跳过重复的固定值
            if i > 0 and nums[i] == nums[i - 1]: continue
            #j 和 k 必须在循环内初始化
            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    res.append([nums[i],nums[j],nums[k]])
                # 修正：找到解后，j 和 k 都要移动，并跳过重复值
                    while j < k and nums[j] == nums[j+1]: j += 1#这里的+1停留在重复数字的边界
                    while j < k and nums[k] == nums[k-1]: k -= 1
                    j += 1
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1
        return res
