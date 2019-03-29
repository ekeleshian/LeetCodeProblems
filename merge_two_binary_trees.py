class Solution:
    def mergeTrees(self, t1, t2):
        """
        """
        if t1 is None:
            return t2
						
        stack = []
        stack.append((t1,t2))
        while stack:
            t = stack.pop()
            if t[1] is None:
                continue
            t[0].val += t[1].val
            
            if t[0].left is None:
                t[0].left = t[1].left
            else:
                stack.append((t[0].left,t[1].left))
            
            if t[0].right is None:
                t[0].right = t[1].right
            else:
                stack.append((t[0].right,t[1].right))
        return t1

    def mergeTrees(self, t1, t2):
        if not t1 and not t2: return None
        if t1:
            N1, L1, R1 = t1.val, t1.left, t1.right
        else:
            N1, L1, R1 = 0, None, None
        if t2:
            N2, L2, R2 = t2.val, t2.left, t2.right
        else:
            N2, L2, R2 = 0, None, None

        node = TreeNode(N1+N2)
        node.left = self.mergeTrees(L1, L2)
        node.right = self.mergeTrees(R1, R2)
        return node