# Given two integers A and B, return any string S such that:

# S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
# The substring 'aaa' does not occur in S;
# The substring 'bbb' does not occur in S.

def str_without_3a_3b(A, B):
	list_a = ['a']*A
	list_b = ['b'] *B
	string = []
	def helper(arr_one, arr_two):
		if len(arr_one) == 0 or len(arr_two) == 0:
			while len(arr_one):
				string.append(arr_one.pop())
			while len(arr_two):
				string.append(arr_two.pop())
			return 0	
		elif len(arr_one) > len(arr_two) + 1:
			string.append(arr_one.pop())
			string.append(arr_one.pop())
			string.append(arr_two.pop())
		elif len(arr_two) > len(arr_one) +1:
			string.append(arr_two.pop())
			string.append(arr_two.pop())
			string.append(arr_one.pop())
		else:
			string.append(arr_one.pop())
			string.append(arr_two.pop())
		helper(arr_one, arr_two)
	helper(list_a, list_b)

	return string

print(str_without_3a_3b(1, 3))