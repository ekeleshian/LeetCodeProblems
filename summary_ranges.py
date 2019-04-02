# Given a sorted integer array without duplicates, return the summary of its ranges.

# Example 1:

# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
# Example 2:

# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.

from pdb import set_trace

def summary_ranges(nums):
	first_idx = 0
	last_idx = None
	results = []
	for i in range(1, len(nums)):
		# set_trace()
		if nums[i] == nums[i-1] + 1:
			last_idx = i
		elif last_idx:
			results.append(str(nums[first_idx])+'->'+str(nums[last_idx]))
			first_idx = i
			last_idx = None
		else:
			results.append(str(nums[first_idx]))
			first_idx = i
			last_idx = None
	if first_idx == len(nums) -1:
		results.append(str(nums[first_idx]))
	if last_idx:
		results.append(str(nums[first_idx])+'->'+str(nums[last_idx]))


	return results


print(summary_ranges([0, 1, 2, 4, 5, 7]))

print(summary_ranges([0,2,3,4,6,8,9]))
