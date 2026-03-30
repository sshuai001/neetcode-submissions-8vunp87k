class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_set = set(nums)
        for num in num_set:
            nums.remove(num)
        return nums[0]