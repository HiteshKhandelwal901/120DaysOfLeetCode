# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #loop through the linked list and store the node in an array. Store the node and not Just the val of     #node as the val can be repeated but node cannot be because of next pointer)

    def hasCycle(self, head: ListNode) -> bool:
        curr = head
        visited= []

        if head == None or head.next == None:
            return False

        while curr!= None:
            if curr not in visited:
                visited.append(curr)
            else:
                return True
            curr = curr.next
