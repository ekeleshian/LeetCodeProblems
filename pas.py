def generate(numRows):
	result = []
	def helper(n):
		if n == 1:
			return result.append([1])
		elif n == 2:
			return result.append([1,1])
		else:
			helper(n-1)
			sub_res = [0]*(n-1)
			sub_res[0] = 1
			sub_res[n-2] = 1
			for i in range(len(result[n-1])-1):
				sub_res[i+1] = result[n-1][i] + result[n-1][i+1]
			return result.append(sub_res)

	result = helper(3)
	print(result)

generate(3)