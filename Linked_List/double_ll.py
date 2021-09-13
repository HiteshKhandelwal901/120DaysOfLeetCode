class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None




class Double_LinkedList(object):
    """docstring forDouble_LinkedList."""

    def __init__(self):
        self.head = None

    def Push_at_start(self, data):
        """
        input  :  data to pushed
        result : node inserted at the begining

        """
        #check if empty node
        if self.head == None:
            #this node becomes the head now (first node)
            head = Node(data)
        #No the first node, i.e, first node exists already
        else:
            #create the new node with curr data
            newnode = Node(data)
            #this new node will be inserted at beg, will have next as head
            newnode.next = self.head
            #curr head had prev as none but now will have this new ndoe as prev
            self.head.prev = newnode
            #now let the newnode pushed at beg be the head.
            self.head = newnode
            #for next push, this nserted new node will act as beg/head.

    def Push_at_end(self, data):
        #check if empty
        if self.head == None:
            head = Node(data)
        #Not the first item
        else:
            newnode = Node(data)
            #insert at the end of the head node
            self.head.next = newnode
            #newnode's prev will become head now
            newnode.prev = self.head
            #this new node will now be the head
            self.head = newnode
