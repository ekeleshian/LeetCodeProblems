#3:43 PM
class Solution:
	def anagramMappings(self, A: 'List[int]', B: 'List[int]') --> 'List[int]':
		mappings = []
		for i in range(len(A)):
			mappings.append(B.index(A[i]))
		return mappings
#Finished at 3:50

# Runtime: 36 ms, faster than 90.19% of Python3 online submissions for Find Anagram Mappings.
# Memory Usage: 6.5 MB, less than 93.85% of Python3 online submissions for Find Anagram Mappings.