# 206. Reverse Linked List (Easy)

# Topics: Linked List, Recursion

# Time Complexity: O(n) - You loop through the values in a linear fashion

# Space Complexity: O(1) - No extra data structure is being used to store data

# Time Spent: 00:09:18

# My Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prvs = None
        current = head

        while current:
            next_node = current.next
            current.next = prvs
            prvs = current
            current = next_node

        return prvs

