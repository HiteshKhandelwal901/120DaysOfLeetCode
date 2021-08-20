# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = []
        curr = head

        while curr:
            if curr in visited:
                return curr
            visited.append(curr)
            curr = curr.next
