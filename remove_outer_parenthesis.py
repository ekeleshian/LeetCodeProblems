
"""
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and 
B are valid parentheses strings, and + represents string concatenation.  
For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does 
not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: 
S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the 
primitive decomposition of S.

"""
from pdb import set_trace


# def remove_outer_parentheses(S):
# 	L, R = 0, 0
# 	idx_out = {0}
# 	for idx in range(len(S)):
# 		# set_trace()
# 		if S[idx] == '(':
# 			L+=1
# 		else:
# 			R+=1
# 		if L == R:
# 			idx_out.add(idx)
# 			idx_out.add(idx+1)
# 	set_trace()
# 	return ''.join([char for ind, char in enumerate(S) if ind not in idx_out])


# def remove_outer_parentheses(S):
# 	removedP = ''
# 	open_p_cnt = 0
# 	for le in S:
# 		if le is '(':
# 			open_p_cnt +=1
# 		else:
# 			open_p_cnt -= 1
# 		if open_p_cnt>0 and not (open_p_cnt==1 and le is '('):
# 			set_trace()
# 			removedP+= le


def remove_outer_parentheses(S):
	ret =''
	op = 0
	for ch in S:
		if ch == '(':
			op += 1

			if op == 1:
				continue
			ret+=ch
		elif ch == ')':
			op -= 1
			if op == 0:
				continue
			ret+=ch
	return ret


print(remove_outer_parentheses('(()()(()))'))