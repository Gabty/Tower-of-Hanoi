class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = node

    def pop(self):
        if self.head == None:
            return
        if self.head.next == None:
            data = self.head.data
            self.head = None
            return data
        current = self.head
        while current.next.next != None:
            current = current.next
        data = current.next.data
        current.next = current.next.next
        return data

    def show(self, attr=None):
        if self.head == None:
            return
        current = self.head
        while current != None:
            if not attr:
                print(current.data, end='->')
            else:
                print(getattr(current.data, attr, None), end='->')
            current = current.next
        print()

    def index(self, ind):
        if self.head == None:
            return
        if ind < 0:
            raise IndexError("index cannot be negative")
        current = self.head
        i = 0
        while i != ind:
            if current.next != None:
                raise IndexError("out of range")
            i+=1
            current = current.next
        return current.data
    
    def getIndex(self, data):
        if self.head == None:
            return
        if data == None:
            raise IndexError("No input")
        current = self.head
        i = 0
        while current.data != data:
            current = current.next
            i+=1
        return i
    
    def length(self):
        if self.head == None:
            return 0
        i=0
        current = self.head
        while current != None:
            i+=1
            current = current.next
        return i

    def getLast(self):
        if self.head == None:
            return
        
        current = self.head
        if current.next == None:
            return current.data
        
        while current.next != None:
            current = current.next

        return current.data
    
    def copy(self):
        new_copy = Stack()
        current = self.head

        while current != None:
            new_copy.insert(current.data)
            current = current.next
        return new_copy

    def popleft(self):
        if self.head == None:
            return
        
        data = self.head.data
        self.head = self.head.next
        return data

    def __eq__(self, other):
        current = self.head
        other_current = other.head
        while current and other_current:
            if current.data != other_current.data:
                return False
            current = current.next
            other_current = other_current.next

        return current is None and other_current is None
    
    def __iter__(self):
        if self.head == None:
            return
        
        current = self.head
        while current:
            yield current
            current = current.next

    def __bool__(self):
        if self.head == None:
            return False
        return True
# EXAMPLE ONLY
def main():
    stack = Stack()
    stack.insert(1)
    stack.insert(3)
    stack.insert(4)
    stack.insert(7)
    stack.insert(2)

    stack2 = stack.copy()
    stack.show()
    stack2.show()

if __name__ == '__main__':
    main()