
# Given a set of points in the xy-plane, determine the minimum area of any rectangle formed from these points, with sides not necessarily parallel to the x and y axes.

# If there isn't any rectangle, return 0.
from copy import deepcopy

from pdb import set_trace
import math
def check_perp(array):
	c_array = deepcopy(array)
	#case_one: if lines are vertical and horizontal
	case_one = False
	case_two = False
	line_one = [c_array[0], c_array[1]]
	line_two = [c_array[1], c_array[2]]
	num_one = (line_one[0][1] - line_one[1][1])
	dem_one = (line_one[0][0] - line_one[1][0])
	num_two = (line_one[0][1] - line_one[1][1])
	dem_two = (line_one[0][0] - line_one[1][0])

	check = (num_one == num_two) and (dem_two == dem_one)
	if check:
		case_one = True
		dist_one = math.sqrt((c_array[0][0] - c_array[1][0])**2 + (c_array[0][1] - c_array[1][1])**2)
		dist_two = math.sqrt((c_array[0][0] - c_array[2][0])**2 + (c_array[2][1] - c_array[0][1])**2)

	if not case_one:	
		line_three = [c_array[0], c_array[2]]
		line_four = [c_array[1], c_array[2]]
		slope_three = (line_one[0][1] - line_one[1][1]) / (line_one[0][0] - line_one[1][0])
		slope_four = (line_one[0][1] - line_one[1][1]) / (line_one[0][0] - line_one[1][0])

		check = -1*(1/slope_two)
		if slope_three == check:
			case_two = True
			dist_three = math.sqrt((c_array[0][0] - c_array[2][0])**2 + (c_array[0][1] - c_array[2][1])**2)
			dist_four = math.sqrt((c_array[1][0] - c_array[2][0])**2 + (c_array[2][1] - c_array[1][1])**2)
	
	if case_one:
		# set_trace()
		return ('case_one', array, dist_one, dist_two)
	if case_two:
		return ('case_two', [array[0], array[2], array[1]], dist_three, dist_four)
	else:
		return None


def find_point(res):
	case = res[0]
	coords = res[1]
	if case == 'case_one':

		if [coords[0][0], coords[1][1]] in coords:
			point = [coords[1][0], coords[0][1]]
		else:
			point = [coords[0][0], coords[1][1]]
	elif case == 'case_two':
		if [coords[0][1], coords[0][0]] in coords:
			point = [coords[1][1], coords[1][0]] 
		else:
			point = [coords[0][1], coords[0][0]]
	set_trace()
	return point


inp = [[0,1],[2,1],[1,1],[1,0],[2,0]]

def minAreaFreeRect(points):
	areas = []
	def helper(points):
		if len(points)==0:
			return 0
		try:
			coord_0 = points.pop()
			coord_1 = points.pop()
			coord_2 = points.pop()
		except:
			return 0

		x_0, y_0 = coord_0[0], coord_0[1]
		x_1, y_1 = coord_1[0], coord_1[1]
		x_2, y_2 = coord_2[0], coord_2[1]
		# one_two = False
		# zero_one = False
		# zero_two = False

		if x_0 == x_1:
			res = check_perp([coord_0, coord_1, coord_2])
			# zero_one = True
		elif x_1 == x_2:
			res = check_perp([coord_1, coord_2, coord_0])
			# one_two = True
		elif x_0 == x_2:
			res = check_perp([coord_0, coord_2, coord_1])

		else:
			res = None

		if res:
			point = find_point(res)

			if point in points:
				area = res[2]*res[3]
				areas.append(area)
			else:
				return helper(points)
		else:
			return helper(points)

	helper(points)
	return areas

print(minAreaFreeRect(inp))