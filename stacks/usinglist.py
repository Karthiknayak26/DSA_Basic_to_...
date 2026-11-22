class stack:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if stack.isempty(self):
            print("empty")
        else:
            print(self.stack.pop())
    def peek(self):
        print(self.stack[-1])
    def display(self):
        print(self.stack)
    def isempty(self):
        if len(self.stack)==0:
            return True
        else:
            return False
        

s=stack()
s.push(10)
s.pop()
s.push(30)
s.peek()
s.display()
s.push(10)
s.push(20)
s.push(30)

print(s.isempty())

s.pop()
s.pop()

print(s.peek())
print(s.isempty())
