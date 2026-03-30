class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0
        for num in num_set:
            if num - 1 not in num_set:
                start = num 
                length = 1
                while start + 1 in num_set:
                    length += 1
                    start += 1
                max_length = max(max_length,length)
        return max_length
  
