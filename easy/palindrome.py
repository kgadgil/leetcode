# 9. Palindrome Number
# Easy

# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1
 

# Follow up: Could you solve it without converting the integer to a string?

def palindrome(x: int) -> bool:
	y = str(x)
	flipped = y[::-1]
	if y == flipped:
		return True
	else:
		return False

def palindrome2(x: int) -> bool:
	if x < 0:
		return False
	rev = 0
	tmp = x
	while tmp!=0:
		digit = tmp % 10
		rev = rev*10 + digit
		tmp //= 10
	return rev == x


def main():
	print(palindrome(121))
	print(palindrome(-121))
	print(palindrome2(121))
	print(palindrome2(400))
	print(palindrome2(4004))

if __name__ == '__main__':
	main()