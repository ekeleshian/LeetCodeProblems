from pdb import set_trace


# def initialize(N):
# 	vec = [i for i in range(N)]
# 	return vec

# def find(vec, idx_one, idx_two):
# 	if vec[idx_one] == vec[idx_two]:
# 		return True
# 	return False

# def union(vec,idx_one, idx_two):
# 	vec[idx_one].append(idx_two)
# 	vec[idx_two].append(idx_one)



# vec = initialize(10)

# union(vec, 10, 9, 3)


def equationsPossible(equations):
	graph = [[] for _ in range(26)]
	for eqn in equations:
		if eqn[1] == '=':
			x = ord(eqn[0]) - ord('a')
			y = ord(eqn[3]) - ord('a')
			graph[x].append(y)
			graph[y].append(x)
	color = [None]*26
	t =0
	for start in range(26):
		if color[start] is None:
			t+=1
			stack = [start]
			while stack:
				set_trace()
				node = stack.pop()
				for nei in graph[node]:
					if color[nei] is None:
						color[nei] = t
						stack.append(nei)

	for eqn in equations:
		if eqn[1] == '!':
			x = ord(eqn[0]) - ord('a')
			y = ord(eqn[3]) - ord('a')
			set_trace()
			if x == y: return False
			if color[x] is not None and color[x] == color[y]:
				return False
	return True
	# for eqn in equations:
	# 	if eqn[1]!= '!':
			
	set_trace()




	# return check


# ex_one = ["a==b", "b!=c", "a==c"]

# ex_two = ["c==c", "b==d", "x!=z"]

# ex_three = ["a==b", "b==c", "a==c"]

# ex_four = ['a!=a']
ex_five= ["b==b","b==e","e==c","d!=e"]

ex_six = ["e==e","d!=e","c==d","d!=e"]

print(equationsPossible(ex_five))


# print(equationsPossible(ex_one))


# print(equationsPossible(ex_six))

# print(equationsPossible(ex_five))
from collections import defaultdict


# class Graph:
# 	def __init__(self, vertices):
# 		self.V = vertices
# 		self.graph = defaultdict(list)

# 	def addEdge(self, u, v):
# 		self.graph[u].append(v)

# 	def find_parent(self, parent, i):
# 		if parent[i] == -1:
# 			return i
# 		if parent[i] != -1:
# 			return self.find_parent(parent, parent[i])

# 	def union(self, parent, x,y):
# 		x_set = self.find_parent(parent, x)
# 		y_set = self.find_parent(parent, y)
# 		parent[x_set] = y_set


# g = Graph(4)

# g.addEdge(0,1)
# g.addEdge(1, 2)
# g.addEdge(2, 3)
# set_trace()