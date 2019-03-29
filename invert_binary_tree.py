class Solution:
    def invertTree(self, root: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        else:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root



# Runtime: 36 ms, faster than 75.62% of Python3 online submissions for Invert Binary Tree.
# Memory Usage: 12.5 MB, less than 51.64% of Python3 online submissions for Invert Binary Tree.