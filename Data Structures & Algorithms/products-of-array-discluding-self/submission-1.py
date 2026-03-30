class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [1] * len(nums)
        right_product = [1] * len(nums)
        
        for i in range(1, len(nums)):
            left_product[i] = left_product[i - 1] * nums[i - 1]
        for i in reversed(range(len(nums) - 1)):
            right_product[i] = right_product[i + 1] * nums[i + 1]
            
        return [l * r for l, r in zip(left_product,right_product)]

