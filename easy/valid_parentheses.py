from collections import deque
# 20. Valid Parentheses
# Solved
# Easy
# Topics
# Companies
# Hint
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

def isValid(s: str) -> bool:
	d = {"(":")", "[":"]", "{":"}"}
	stack = []
	if len(s) == 0:
		return False
	for i in s:
		if i in d:
			stack.append(i)
		elif len(stack) == 0 or d[stack.pop()] != i:
			return False
	return len(stack) == 0



def main():
	print(isValid("()"))
	print(isValid("()[]{}"))
	print(isValid("([]{}"))
	print(isValid("(]"))

if __name__ == '__main__':
	main()