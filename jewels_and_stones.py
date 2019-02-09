#11:44 AM
from collections import Counter
class Solution:
	def numJewelsInStones(self, J: 'str', S: 'str') --> 'int':
		J_set = set('+'.join(J).split('+')) #letters are guaranteed distinct
		S_dict = Counter(S)
		total_jewels = 0
		for elem in J_set:
			if elem in S_dict:
				total_jewels += S_dict[elem]
		return total_jewels

#12:05


# Runtime: 40 ms, faster than 86.28% of Python3 online submissions for Jewels and Stones.
# Memory Usage: 6.5 MB, less than 16.31% of Python3 online submissions for Jewels and Stones.




