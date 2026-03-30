class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #哈希表问题,将列表中的字符串排序,如果是异位词的话排序后相同,然后遍历排序后的列表
        #将排序后的字符串作为键,未排序的字符串作为值,最后返回所有值
        from collections import defaultdict
        res = defaultdict(list)

        for s in strs:
            #sorted(s) 返回 list，必须 join 成字符串
            key = ''.join(sorted(s))
            #试用append防止单词被覆盖
            res[key].append(s)
        return list(res.values())
