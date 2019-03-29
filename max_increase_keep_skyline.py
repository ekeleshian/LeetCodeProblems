grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]

from pdb import set_trace

def max_increase_keep_skyline(grid):
	num = len(grid)
	max_rows = []
	max_cols = []
	max_dict = []
	total = 0
	for idx, r in enumerate(grid):
		max_rows.append(max(r))
	potential_max = 0
	for c in range(num):
		for r in range(num):
			if grid[r][c] > potential_max:
				potential_max = grid[r][c]
		max_cols.append(potential_max)
		potential_max = 0

	max_list = list(zip(max_rows, max_cols))

	for row in range(num):
		relevant_one = max_rows[row]
		for col in range(num):
			# set_trace()
			relevant_two = max_cols[col]
			repl = min(relevant_two, relevant_one)
			old = grid[row][col]
			diff = repl - old
			total+= diff
			grid[row][col] = repl
			# set_trace()

	# print(total)
	return total




print(max_increase_keep_skyline(grid))





