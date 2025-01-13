# 2. Add Two Numbers
# Solved
# Medium
# Topics
# Companies
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
	# Why Use Static Methods?

    # Self-Contained: These methods don't depend on the instance state (e.g., instance variables), so marking them as @staticmethod is appropriate.
    # Readability: Keeping them in the Solution class maintains contextual relevance (they are helper methods specifically for working with linked lists in this problem).
    # Encapsulation: Including the helper methods in the class encapsulates all logic related to solving the problem.
	@staticmethod
	def create_linked_list(values):
		"""Helper method to create a linked list from a list of values."""
		dummy_head = ListNode(0)
		current = dummy_head
		for value in values:
			current.next = ListNode(value)
			current = current.next
		return dummy_head.next

	@staticmethod
	def linked_list_to_list(node):
	    """Helper method to convert a linked list to a Python list."""
	    result = []
	    while node:
	        result.append(node.val)
	        node = node.next
	    return result

	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		# initialize dummy node and carry
		# while there is a node in either l1 or l2 or carry exists
		# add the first nodes values and carry
		# update carry to be sum floor-divided by 10
		# save this new value in the next node of dummy
		# move dummy one node to the right
		# move l1 and l2 one node to the right
		dummy = ListNode()
		curr = dummy
		carry = 0
		while l1 != None or l2 != None or carry != 0:
			first = l1.val if l1 else 0
			second = l2.val if l2 else 0
			colSum = first + second + carry
			carry = colSum // 10
			curr.next = ListNode(colSum % 10)
			curr = curr.next
			l1 = l1.next if l1 else None
			l2 = l2.next if l2 else None
		return dummy.next

def main():
    # Define test inputs
    l1_values = [2, 4, 3]  # Represents the number 342
    l2_values = [5, 6, 4]  # Represents the number 465
    
    # Create linked lists
    solution = Solution()
    l1 = Solution.create_linked_list(l1_values)
    l2 = Solution.create_linked_list(l2_values)
    
    # Call the solution method
    result = solution.addTwoNumbers(l1, l2)
    
    # Convert result back to a Python list and print
    print("Result:", Solution.linked_list_to_list(result))  # Output should be [7, 0, 8]

if __name__ == "__main__":
    main()
