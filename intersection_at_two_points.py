class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSymmetric(root):
	l_stack = []
	l_results=[]
	if root.left:
		return helper(root.left, 'left')
	def helper(rt, dir):
		if dir == 'left':
			if rt.left:
				l_stack.append(rt)
				helper(rt.left, dir)
			parent = l_stack.pop()
			if parent.right:

				helper(rt.right,dir)

