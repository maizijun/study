class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque

        self.stack = deque()


    def push(self, x):
        """
        Push element x onto stack.
        """
        self.stack.append(x)
    
        # return self.stack 


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.stack.pop()


    def top(self):
        """
        Get the top element.
        """
        return self.stack[-1] if self.stack else -1


    def empty(self):
        """
        Returns whether the stack is empty.
        """
        return len(self.stack)==0



# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
print(obj)
param_2 = obj.pop()
param_3 = obj.top()
# param_4 = obj.empty()