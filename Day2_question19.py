class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size = 1
        curr = head
        while(curr.next!=None):
            size = size + 1
            curr = curr.next
            #print(curr.val)
        print("size = ", size)
        nth = size - n
        print("nth = ", nth)

        curr = head
        i=1
        while i< nth:
            print("i = ", i)
            i=i+1
            curr = curr.next

        if size>1:
            if nth>0:
                print("nth >0 ")
                delnode = curr.next
                #print("delnode  = ", delnode.val)
                addnode = delnode.next
                #print("addnode = ", addnode.val)
                curr.next = addnode
                #print("curr.next.val = ", curr.next.val)
                #print("delted list = ", head)
                return head
            else:
                print("nth < 0")
                head = curr.next
                print("head")
                return head
        else:
            head = None
            return head
