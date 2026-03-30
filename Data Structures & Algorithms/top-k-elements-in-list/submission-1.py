class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []
        buckets = [[] for _ in range(len(nums) + 1)]
        #将数字填到对应出现次数的桶中
        for num, freq in count.items():
            buckets[freq].append(num)
        
        for bucket in reversed(buckets):
            for num in bucket:
                if len(res) == k:
                    return res
                res.append(num)
        return res
        