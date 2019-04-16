from pdb import set_trace

"""
Given the root node of a binary search tree, return the sum of values of all 
nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique value

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

"""

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def range_sum_BST(root, L, R):
	visited = []
	def helper(root):
		# set_trace()
		if root:
			if root.val == L:
				visited.append(root.val)
				# return
			elif root.val == R:
				visited.append(root.val)
				# return
			elif root.val > L and root.val < R:
				visited.append(root.val)
				helper(root.left)
				helper(root.right)
			else:
				helper(root.left)
				helper(root.right)

	helper(root)
	# set_trace()
	return sum(visited)

tree = TreeNode(10)
tree.left = TreeNode(5)
tree.right = TreeNode(15)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(7)
tree.right.right = TreeNode(18)


tree_two = TreeNode(10)
tree.left = TreeNode(5)
tree.right = TreeNode(15)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(7)
tree.right.left = TreeNode(13)
tree.right.right = TreeNode(18)
tree.left.left.left = TreeNode(1)
tree.left.right.left = TreeNode(6)


print(range_sum_BST(tree_two, 6, 10))

