# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    
    def match(self, root: TreeNode, subRoot: TreeNode) -> bool:
        
        if(not subRoot):
            if(root):
                return False
            return True
        
        if(not root):
            return False
        
        if(root.val != subRoot.val):
            return False
        
        return (self.match(root.left, subRoot.left) and self.match(root.right, subRoot.right))
    
        
    def pre_order(self, root: TreeNode, subRoot: TreeNode) -> None:
        
        self.ans = self.ans or self.match(root, subRoot)
        if(root.left):
            self.pre_order(root.left, subRoot)
        if(root.right):
            self.pre_order(root.right, subRoot)
    
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        
        self.ans = False
        self.pre_order(root, subRoot)
        return self.ans