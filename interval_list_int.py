from pdb import set_trace
from copy import deepcopy

# Definition for an interval.
class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e


def intervalIntersection(A, B):
	seen = []
	for intr_a in A:
		for intr_b in B:
			max_lb = max([intr_a.start, intr_b.start])
			min_ub = min([intr_a.end, intr_b.end])
			# set_trace()
			if max_lb <= min_ub and (max_lb, min_ub) not in seen:
				seen.append((max_lb, min_ub))

	results = []
	for coords in seen:
		results.append([coords[0], coords[1]])

	set_trace()




A = [Interval(0,2), Interval(5,10),Interval(13,23), Interval(24,25)]
B = [Interval(1,5), Interval(8,12),Interval(15,24),Interval(25,26)]

intervalIntersection(A, B)