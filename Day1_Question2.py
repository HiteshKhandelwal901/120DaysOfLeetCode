# Definition for singly-linked list.

 class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        #l1 --> List 1, L2 --> List 2, Sumode --> resultant linked list, curr -- > pointer
        carry = 0
        #Create a preceding zero node fro convience
        sumNode = ListNode(0)
        #start the pointer from this zero node
        curr = sumNode
        #check if elements are there in both the lists or if there is a carry (edge case)
        while l1 or l2 or carry:
            #if value in l1 exists get it else mark it as zero. same in l2
            if l1:
                l1val  = l1.val
            else:
                l1val = 0

            if l2:
                l2val = l2.val
            else:
                l2val = 0

            # if the curr sum in the curr column including carry is lesse than9
            # do tsratight additon and store the result in res node
            if l1val + l2val+carry <=9:
                summ = int((l1val + l2val + carry))
                carry= int((l1val + l2val + carry)/10)
                res = ListNode(summ)
            else:
                # if sum >9 , we need to get result sum of curr colm by taking
                # mod and carry will be the quotient.
                res = ListNode(int((l1val + l2val + carry)%10))
                carry= int((l1val + l2val + carry)/10)

            # curr is a pointer of a sumNode linked list. in the start it points
            #  to zero node, in each iteration update the link and move the pointer
            curr.next = res
            curr = curr.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        return sumNode.next
