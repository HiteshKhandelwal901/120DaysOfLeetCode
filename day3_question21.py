# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3  = None


        while(l1 and l2):
            if l1.val <= l2.val:
                if l3 == None:
                    print("inside none with l3 = ", l3)
                    l3 = l1
                    print("l3 after update = ", l3)
                    ptr = l3
                    print("ptr = ", ptr)
                else:
                    ptr.next = l1
                    print("ptr,next = ", ptr.next)
                    ptr = ptr.next
                    print("upfated ptr = ", ptr)
                l1 = l1.next
                print("updated l1 = ", l1)

            else:
                if l3 == None:
                    print("inside else l3 == none")
                    l3 = l2
                    print("updated l3 = ", l3)
                    ptr = l3
                    print("ptr = ",  ptr)
                else:
                    ptr.next = l2
                    print("inside else with ptr next = ", ptr.next)
                    ptr = ptr.next
                    print("updated pointer = ", ptr)

                l2 = l2.next
                print("updated l2 = ", l2)

        if l1:
            #final.append(curr1.val)
            if l3==None:
                l3 = l1
            else:
                ptr.next = l1
        else:
            if l3 == None:
                l3 = l2
            else:
                ptr.next = l2
        return l3
