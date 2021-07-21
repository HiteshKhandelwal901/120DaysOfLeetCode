# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        sumNode = ListNode(0)
        curr = sumNode
        while l1 or l2 or carry:
            #print("inside while")
            #print("l1 val and l2 val before = ", l1.val,l2.val)
            #print("check if l1 == true, i,e", l1, " == ", True)
            if l1:
                #print("result true")
                l1val  = l1.val
            else:
                #print("result false")
                l1val = 0

            if l2:
                l2val = l2.val
            else:
                l2val = 0
            #print("l1val = ", l1val, "l2val = ", l2val)

            #print("type l1 and l2  = ", type(l1), type(l2))

            if l1val + l2val+carry <=9:
                #print("summing ", l1val , " + ", l2val)
                #print("type = ", type(carry), " type = ", type(l1val))
                summ = int((l1val + l2val + carry))
                carry= int((l1val + l2val + carry)/10)
                #print("ans = ",summ)
                #print("carry = ", carry)
                res = ListNode(summ)
            else:
                #print("summing ", l1val , " + ", l2val)
                res = ListNode(int((l1val + l2val + carry)%10))
                #print("ans = ", (l1val + l2val + carry)%10)
                carry= int((l1val + l2val + carry)/10)
                #print("carry = ", carry)

            curr.next = res
            curr = curr.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        return sumNode.next
