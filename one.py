class node:
    def __init__(self, data=None):
        self.data = data 
        self.next = None 
class linked_list:
    def __init__(self):
        self.head = node()

    def append(self,data):
        temp = node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = temp
    
    def insertUpFront(self,data):
        temp = self.head.next
        new = node(data)
        self.head.next = new
        new.next = temp
    
    def delete(self,data):
        start = self.head.next
        temp = self.head 
        while start is not None:
            if start.data == data:
                return temp.next = start.next
            else:
                start = start.next
                temp = temp.next
    
    def findNode(self,data):
        temp = self.head.next
        while temp is not None:
            if temp.data == data:
                return temp
            temp = temp.next
        return "The Node is not found in the list"

    def remove(self):
        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None

    def length(self):
        current = self.head
        size = 0
        while current.next != None:
            size += 1
            current = current.next 
        return size 

    def display(self):
        temp = []
        current = self.head 
        while current.next != None:
            current = current.next
            temp.append(current.data)
        print (temp)
    
    def getIndex(self,index):
        if index >= self.length():
            return "The index is out of range"
        temp = self.head.next
        pos = 0
        while pos != index:
            temp = temp.next 
            pos += 1
        return temp
    
    def getMiddle(self):
        if self.length() % 2 == 0: 
            ans = self.getIndex(self.length() / 2)
        else: ans = self.getIndex(((self.length() + 1) / 2) - 1)
        return ans

    def getMiddleNode(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def getMiddleList(self):
        middle_list = []
        if self.length() % 2 == 0: 
            temp = self.getIndex(self.length() / 2)
            while temp.next != None:
                middle_list.append(temp.data)
            return middle_list
        temp = self.getIndex(((self.length() + 1) / 2) - 1)
        while temp != None:
            middle_list.append(temp.data)
            temp = temp.next
        return middle_list 
    
    def reverseList(self):
        start = self.head
        rev = linked_list()
        while start.next != None:
            temp = self.head.next
            while temp.next != None:
                temp = temp.next
            rev.append(temp.data)
            self.remove()
        return rev
    
    def merge_Slist(self,l2):
        p1 = self.head.next
        p2 = l2.head.next
        final = linked_list()
        while p1 or p2:
            if p1 == None:
                final.append(p2.data)
                p2 = p2.next
            elif p2 == None:
                final.append(p1.data)
                p1 = p1.next
            elif p1.data < p2.data:
                final.append(p1.data)
                p1 = p1.next
            elif p1.data == p2.data:
                final.append(p1.data)
                p1 = p1.next
                p2 = p2.next
            else:
                final.append(p2.data)
                p2 = p2.next
        final.display()
    
    def remove_duplicates(self):
        start = self.head.next
        temp = self.head.next.next
        while temp != None:
            if start.data == temp.data:
                start.next = temp.next
                temp = temp.next
            else:
                start = start.next 
                temp = temp.next
        self.display()
    
    def hasCycle(self):
        start = self.head.next
        nodes = {}
        while start.next != None:
            if start in nodes:
                return True
            nodes[start] = start.data
            start = start.next
        return False 

  
