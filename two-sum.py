from typing import List
# 1. Two Sum

# Hint
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists

def twoSum(nums: List[int], target: int) -> List[int]:
	# brute force
	# O(n^2) time | O(1) space
	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			sum = nums[i] + nums[j]
			if sum == target:
				return [i, j]

def twoSum2(nums: List[int], target: int) -> List[int]:
	# initiliaze a dictionary
	# enumerate nums, if target minus the current number is already in the dictionary, return that number and current index
	# if not, add the current number to the dictionary
	# O(n) time | O(n) space
	d = {}
	for i, num in enumerate(nums):
		if target - num in d:
			return [d[target - num], i]
		d[num] = i

def twoSum3(nums: List[int], target: int) -> List[int]:
	# two pointers
	# O(n) time | O(1) space
	i=0
	j=i+1
	while i<len(nums) and j<len(nums):
		if nums[i]+nums[j]==target:
			return [i,j]
		elif nums[i]+nums[j]<target:
			i+=1
		else:
			j+=1

def main():
	print(twoSum([2,7,11,15], 9))
	# print(twoSum([3,2,4], 6))
	# print(twoSum([3,3], 6))
	print(twoSum2([2,7,11,15], 9))
	print(twoSum3([2,7,11,15], 9))

if __name__ == '__main__':
	main()
