# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def traverse(self, root, listed):
        if root:
            self.traverse(root.left, listed)
            listed.append(root.val)
            self.traverse(root.right, listed)
        
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        listed = []
        self.traverse(root,listed)
        return listed
    
