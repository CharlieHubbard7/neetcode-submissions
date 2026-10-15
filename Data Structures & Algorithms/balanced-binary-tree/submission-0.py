# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if (root == None):
            return True
        else:
            diff = self.getHeight(root.left) - self.getHeight(root.right)
            if (diff > 1 or diff < -1): return False
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getHeight(self, root):
        if (root == None):
            return 0
        else:
            return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        