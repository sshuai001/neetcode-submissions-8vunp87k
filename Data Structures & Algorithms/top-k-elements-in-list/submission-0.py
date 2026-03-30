class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #桶排序版本
        hashmap = {}
        res = []
        buckets = [[] for i in range(len(nums) + 1)]
        #将所有num与对应的freq加入到哈希表中
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        for num, freq in hashmap.items():
            buckets[freq].append(num)
        for i in range(len(buckets) - 1, 0, -1):
            # i 就是当前的频次
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
