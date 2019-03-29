# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

# def find_ways(array):
# 	results = {}
# 	while j < len(array):


from copy import deepcopy


def climb_stairs(n):
	base = [1]*n
	level = 0
	def helper(base, start, stop):
		if len(base) == 1:
			return [1]
		

		






		return result
	soln = helper(base[1:], n-1)



print(climb_stairs(5))




