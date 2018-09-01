class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self, top = None):
        self.top = top
    
    def push(self, data):
        self.top = Node(data, self.top)
    
    def pull(self):
        if self.top is None:
            return None
        temp = self.top.data
        self.top = self.top.next
        return temp
    
    def peek(self):
        return None if self.top is None else self.top.data
    
    def IsEmpty(self):
        return self.peek() is None

