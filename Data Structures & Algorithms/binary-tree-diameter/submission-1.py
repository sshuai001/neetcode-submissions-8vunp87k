# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        #dfs返回的是深度，而结果要返回最大直径，所以需要一个内部的递归函数
        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            #节点作为根时计算左右深度与当前最大值比较
            self.res = max(self.res, left + right)
            
            return 1 + max(left, right)
        dfs(root)
        return self.res