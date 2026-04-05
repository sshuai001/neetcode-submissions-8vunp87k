# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #辅助函数判断是否是同一棵树
    def sameTree(self, tree, subtree):
        if not tree and not subtree:
            return True
        if tree and subtree and tree.val == subtree.val:
            return self.sameTree(tree.left, subtree.left) and self.sameTree(tree.right, subtree.right)
        return False  
         
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot)


        