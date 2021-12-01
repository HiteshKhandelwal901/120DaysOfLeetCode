"""
We use two pointers here, the slow pointer loops through each node and while
slow pointer mal\kes one loop, we move the runner from the slow pointer to the end 
and check if the data is equal to the one pointed by slow pointer and if yes
we remove it
"""

def remove_node_without_buffer(head):
    #slow pointer 
    curr = head
    while curr!= None:
        #runner is fast pointer
        runner = curr
        #loop fast pointer from slow pointer's location to the end 
        while(runner!=None):
            if runner.next.data == curr.data:
                runner.next = curr.next.next
            else:
                runner = runner.next
    return head