class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        newnode = Node(data)
        newnode.next = self.top
        self.top = newnode

    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            deleted = self.top.data
            self.top = self.top.next
            print("Deleted:", deleted)

    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top:", self.top.data)

    def display(self):
        current = self.top

        while current is not None:
            print(current.data)
            current = current.next


s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()
s.pop()
s.display()
s.peek()