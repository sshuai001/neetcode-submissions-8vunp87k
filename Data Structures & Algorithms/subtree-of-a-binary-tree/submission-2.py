# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #辅助函数判断是否是同一棵树
    def sameTree(self, curr, subTree):
        if not curr and not subTree:
            return True
        if curr and subTree and curr.val == subTree.val:
            return self.sameTree(curr.left, subTree.left) and self.sameTree(curr.right, subTree.right)
        return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False
        
        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
