from stack import Stack
from random import randint as ran

class Branch:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

class Tree:
    def __init__(self):
        self.top = None
    
    def insert(self, data):
        node = Branch(data)
        if self.top == None:
            self.top = node
            return
        
        current = Stack()
        current.insert(self.top)
        while current:
            branch = current.pop()
            if branch.left:
                current.insert(branch.left)
            else:
                branch.left = node
                break

            if branch.right:
                current.insert(branch.right)
            else:
                branch.right = node
                break
    

    def show(self):
        if self.top == None:
            return
        stack = Stack()
        branch = self.top
        while stack or branch:
            while branch:
                stack.insert(branch)
                branch = branch.left
            branch = stack.popleft()
            yield branch.data
            branch = branch.right
    def __len__(self):
        i = 0
        stack = Stack()
        branch = self.top
        while stack or branch:
            while branch:
                stack.insert(branch)
                branch = branch.left
            branch = stack.popleft()
            i+=1
            branch = branch.right
        return i
    def __str__(self):
        string = '['
        stack = Stack()
        branch = self.top
        while stack or branch:
            while branch:
                stack.insert(branch)
                branch = branch.left
            branch = stack.popleft()
            string += str(branch.data)+', '
            branch = branch.right
        string += ']'
        return string
print(__name__)
#example
if __name__ == '__main__':
    t = Tree()
    for i in range(100):
        t.insert(i)
    
    print(t)

    