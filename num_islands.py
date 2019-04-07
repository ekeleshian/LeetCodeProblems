from pdb import set_trace

def get_neighs(coords, seen):
	x, y = coords
	neighbs = []
	if (x+1, y) in seen:
		neighbs.append((x+1, y))
	if (x, y+1) in seen:
		neighbs.append((x, y+1))
	if (x-1, y) in seen:
		neighbs.append((x-1, y))
	if (x, y-1) in seen:
		neighbs.append((x, y-1))
	return neighbs

def numIslands(grid):
	mrows = len(grid)
	ncols = len(grid[0])
	seen = set()
	for idx in range(mrows):
		for jdx in range(ncols):
			if grid[idx][jdx] == '1':
				seen.add((idx, jdx))

	num_islands = 0

	color = [[0 for _ in range(ncols)] for _ in range(mrows)]
	t= 0
	for idx in range(mrows):
		for jdx in range(ncols):
			if (idx, jdx) in seen:
				if color[idx][jdx] == 0:
					t+=1
					color[idx][jdx] = t
					stack = [(idx, jdx)]
					while stack:
						coords = stack.pop()
						neighs = get_neighs(coords, seen)
						for tup in neighs:
							if color[tup[0]][tup[1]] == 0:
								stack.append(tup)
								color[tup[0]][tup[1]] = t
					# set_trace()
	set_trace()

	uniq_colors = set()
	for row in color:
		for elem in row:
			if elem != 0:
				uniq_colors.add(elem)


	return len(uniq_colors)
# island_one = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

island_one = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
island_two = [["1","1","1"],["0","1","0"],["1","1","1"]]
print(numIslands(island_two))