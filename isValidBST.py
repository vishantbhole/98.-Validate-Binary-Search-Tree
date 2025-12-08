# 98. Validate Binary Search Tree
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        min = float("-infinity")
        max = float("infinity")
        def valid(node,left,right):
            if not node:
                return True
            if not(node.val < right and node.val > left):
                return False

            return (valid(node.left, left, node.val) and
                    valid(node.right,node.val, right))
