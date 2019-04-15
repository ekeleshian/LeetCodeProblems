from pdb import set_trace
from copy import deepcopy

def partition_labels(S):
	"""
	A string S of lowercase letters is given. Partition string into as many parts as possible
	so that each letter appears in at most one part, and return a list of integers representing 
	the size of these parts

	Input: S = "ababcbacadefegdehijhklij"
	Output: [9,7,8]
	Explanation:
	The partition is "ababcbaca", "defegde", "hijhklij".
	This is a partition so that each letter appears in at most one part.
	A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
	"""
	last = {char: idx for idx, char in enumerate(S)}
	jdx = anchor = 0
	ans = []
	# set_trace()
	for idx, char in enumerate(S):
		# set_trace()
		jdx = max(jdx, last[char])
		set_trace()
		if idx == jdx:
			ans.append(idx - anchor +1)
			anchor = idx +1
	return ans


S = "abacbadefegdehijhklij"
partition_labels(S)
