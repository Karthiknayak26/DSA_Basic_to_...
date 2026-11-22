class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlylinkedlist:
    def __init__(self):
        self.head=None
    
    def add_at_begin(self,data):
        newnode=node(data)
        newnode.next=self.head
        self.head=newnode

    def display(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next

    def insert_at_tail(self,data):
        newnode=node(data)
        current=self.head
        if self.head is None:
            self.head=newnode
            return
        elif self.head is not None:
            while current.next is not None:
                current=current.next
            current.next=newnode
            newnode.next=None
    def del_at_head(self):
        if self.head==None:
            print("list is empty")
            return
        else:
            self.head=self.head.next
    
    def del_at_tail(self):
        current=self.head
        if self.head is None:
            print("ntg to delete")
        else:
            while current.next.next is not None:
                            current=current.next
            current.next=None

    def insert_after_node(self,given_data,data):
        current=self.head
        newnode=node(data)
        while current is not None:
            if current.data == given_data:
                newnode.next=current.next
                current.next=newnode
                return
            current=current.next
        print("not found")

    def delete_after_node(self,given_data):
        current=self.head
        while current is not None:
            if current.data == given_data:
                if current.next is None:
                    print("no node exist")
                    return
                current.next=current.next.next
            current=current.next

    def search(self,key):
        current=self.head
        while current is not None:
            if current.data==key:
                print("found")
            current=current.next
        return False

ll=singlylinkedlist()
# ll.add_at_begin(10)
# ll.add_at_begin(20)
# ll.add_at_begin(30)
# ll.insert_at_tail(40)
# ll.insert_at_tail(50)
# ll.insert_at_tail(60)
# ll.del_at_head()
# ll.del_at_tail()
# ll.insert_after_node(50,70)
# ll.display()
# print("")
# ll.delete_after_node(20)
# ll.search(20)
# ll.display()

while True:
    print("1. Insert at beginning")
    print("2. Insert at tail")
    print("3. Delete at beginning")
    print("4. Delete at tail")
    print("5. Search")
    print("6. Display")
    print("7. Exit")

    choice=int(input("enter the choice"))

    if choice ==1:
        val=int(input("enter the value"))
        ll.add_at_begin(val)

    elif choice == 2:
        # Call tail insertion method
        val=int(input("enter the value"))
        ll.insert_at_tail(val)


    elif choice == 3:
        # Call deletion method
        ll.del_at_head()


    elif choice == 4:
        # Call tail deletion method
        ll.del_at_tail()


    elif choice == 5:
        # Call search method
        val=int(input("enter the value"))
        ll.search(val)


    elif choice == 6:
        # Call display method
        ll.display()


    elif choice == 7:
        break

    else:
        print("Invalid choice")



