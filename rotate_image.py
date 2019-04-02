# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).

# Note:

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
from pdb import set_trace

def rotate(matrix):
	temp_matrix = []
	transpose = []
	reverse = list(range(len(matrix)-1, -1, -1))
	for idx in reverse:
		temp_matrix.append(matrix[idx].copy())

	for idx, row in enumerate(temp_matrix):
		transpose.append([temp_matrix[jdx][idx] for jdx, junk in enumerate(row)])

	for idx, row in enumerate(matrix):
		for jdx, col in enumerate(matrix):
			matrix[idx][jdx] = transpose[idx][jdx]

	return matrix

	# return matrix

matrix = [[1,2], [3,4]]


print(rotate(matrix))

# transpose = []

# for idx, row in enumerate(matrix):
# 	set_trace()
# 	transpose.append([ matrix[i][idx] for i, junk in enumerate(row)])

# print(transpose)

