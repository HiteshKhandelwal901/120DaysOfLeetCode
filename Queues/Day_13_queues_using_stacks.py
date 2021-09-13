class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue. O(n)
        """

        #pop all the elements from s1 to s2.Ex:  S1 [1], x = 2 then s2 = [1] -> s1 = [2] -> s1 = [2,1]
        while self.s1:
            self.s2.append(self.s1.pop())
        #append the latest entry x to the lowest in the stack
        self.s1.append(x)

        #copy all the elements from s2 to s1 again
        while self.s2:
            self.s1.append(self.s2.pop())


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element. o(1)
        """
        return self.s1.pop()

    def peek(self) -> int:
        """
        Get the front element. O(n)
        """
        #front element is the lowest  element in the stack
        return self.s1[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty. O(n)
        """

        if self.s1:
            return False
        return True



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
