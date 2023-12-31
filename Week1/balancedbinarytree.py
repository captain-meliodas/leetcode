#Link -> https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) != -1
    
    def height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left_height = self.height(root.left)
        if left_height == -1:
            return -1

        right_height = self.height(root.right)
        if right_height == -1:
            return -1
        
        if abs(left_height-right_height) <= 1:
            return max(left_height,right_height) + 1
        else:
            return -1