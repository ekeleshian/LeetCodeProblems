from pdb import set_trace

# def first(queue):
# 	first = queue[0]
# 	queue = queue[1:]
# 	return first

# def graph_neighbs(row, col):
# 	hit_wall_east = False
# 	hit_wall_north = False
# 	if row > len(matrix) - 1:
# 		hit_wall_east = True
# 	if col > len(matrix[0]) -1:
# 		hit_wall_north = True
# 	if hit_wall_east:
# 		return ((None, None), (row, col+1))
# 	elif hit_wall_north:
# 		return ((row+1, col), (None, None))
# 	else:
# 		return ((row+1, col), (row, col+1))

# def updateMatrix(matrix):

# 	def helper(row, col):
# 		counter=0
# 		while queue:
# 			current = first(queue)			
# 			if current == 0:
# 				return counter
# 			counter+=1
# 			for neighb in graph_neighbs(row, col):
# 				if not None in neighb:
# 					queue.append(neighb)
# 		return counter


# 	for idx, row in enumerate(matrix):
# 		for jdx, col in enumerate(row):
# 			queue = [matrix[idx][jdx]]
# 			matrix[idx][jdx]=helper(idx, jdx)
# # 	# set_trace()

matrix = [[0,0,0], [0, 1,0], [1, 1, 1]]

# updateMatrix(matrix)


# print(matrix)

import collections

def updateMatrix(matrix):
	m, n = len(matrix), len(matrix[0])
	queue = collections.deque()
	visited = set()
	for i in range(m):
		for j in range(n):
			if matrix[i][j] == 0:
				visited.add((i, j))
				queue.append((i, j))

	while queue:
		size = len(queue)
		for _ in range(size):
			i, j = queue.popleft()
			if i - 1 >= 0 and (i-1,j) not in visited:
				matrix[i-1][j] = matrix[i][j] + 1
				visited.add((i-1, j))
				queue.append((i-1, j))
			if j - 1 >= 0 and (i,j-1) not in visited:
				matrix[i][j-1] = matrix[i][j] + 1
				visited.add((i, j-1))
				queue.append((i-1, j))
			if i + 1 < m and (i+1,j) not in visited:
				matrix[i+1][j] = matrix[i][j] + 1
				visited.add((i+1, j))
				queue.append((i+1, j))
			if j + 1 < n and (i,j+1) not in visited:
				matrix[i][j+1] = matrix[i][j] + 1
				visited.add((i, j+1))
				queue.append((i, j+1))

	return matrix

print(updateMatrix(matrix))
			