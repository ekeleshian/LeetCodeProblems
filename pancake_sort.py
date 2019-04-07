from pdb import set_trace
from copy import deepcopy


def pancakeSort(A):
	a_copy = deepcopy(A)
	flips = []
	def flip_matrix(i, a_copy, stop):
		flips.append(stop)
		arr_part = a_copy[:stop+1]
		arr_max = a_copy[stop+1:]
		arr_one = arr_part[:i+1]
		arr_two = arr_part[i+1:]
		arr_one.reverse()
		arr_part = arr_one + arr_two
		arr_part.reverse()
		flips.append(len(arr_part))
		a_copy = arr_part+arr_max
		return a_copy
	def helper(a_copy,stop):
		if stop == 0:
			return a_copy
		# set_trace()
		max_idx = a_copy[:stop+1].index(max(a_copy[:stop+1]))
		if max_idx != stop:
			a_copy = flip_matrix(max_idx, a_copy, stop)
		return helper(a_copy, stop-1)




	a_copy = helper(a_copy, len(a_copy)-1)
	set_trace()
	return flips


pancakeSort([195,32,1,6,2,3])