class node:
    def __init__(self,data):
        self.data=data
        self.next=None

n1=node(10)
n2=node(20)
n1.next=n2
print(n1.data)
print(n1.next.data)
