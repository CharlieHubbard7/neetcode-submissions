# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        else:
            return ((self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)))

    def isSameTree(self, root, root2):
        if root == None and root2 == None:
            return True
        elif root != None and root2 != None:
            if root.val != root2.val: return False
            return (self.isSameTree(root.left, root2.left) and 
                    self.isSameTree(root.right, root2.right))
        else: return False

        