from pdb import set_trace

# def generateParenthesis(n):
# 	max_distance = n
# 	# max_distance = n-1
# 	results = [None]*2*n
# 	total = []

# 	def helper(distance,results):
# 		if distance != 1:
# 			helper(distance-2,results)
# 		if None in results:
# 			for idx, elem in enumerate(results):
# 				if elem is None:
# 					pos = idx
# 					# set_trace()
# 					break
# 			results[pos] = "("
# 			results[pos+distance]=")"
# 			# set_trace()
# 			if len(results[pos+distance+1:]) < distance:
# 				helper(distance-2,results)
# 			helper(distance,results)
# 		else:
# 			total.append(results)
# 			results = [None]*2*n


# 	helper(n*2-1, results)
# 		# total.append(''.join(results))
# 	print(total)
# 	return None

# generateParenthesis(3)

def generateParenthesis(num):
	ans = []
	def backtrack(S='', left = 0, right = 0):
		if len(S) == 2*num:
			ans.append(S)
			set_trace()
			return
		if left<num:
			set_trace()
			backtrack(S+'(',left+1, right)
		if right<left:
			set_trace()
			backtrack(S+')', left, right+1)
	backtrack()
	return ans

print(generateParenthesis(2))