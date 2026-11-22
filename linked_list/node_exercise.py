class node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def display(self):
        print(self.data)
        print(self.next)

n1=node(10)
n2=node(20)
n3=node(30)
n1.next=n2
n2.next=n3
n3.next=None
head=n1
current=head
def display(head):
    current=head
    while current is not None :
        print(current.data)
        current=current.next

display(head)
