class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # 1. Insert at beginning
    def insert_at_beginning(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = self.tail = newnode
            return

        newnode.next = self.head
        self.head.prev = newnode
        self.head = newnode

    # 2. Insert at tail
    def insert_at_tail(self, data):
        newnode = Node(data)

        if self.tail is None:
            self.head = self.tail = newnode
            return

        newnode.prev = self.tail
        self.tail.next = newnode
        self.tail = newnode

    # 3. Delete at beginning
    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        deleted = self.head.data

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        print("Deleted:", deleted)

    # 4. Delete at tail
    def delete_at_tail(self):
        if self.tail is None:
            print("List is empty")
            return

        deleted = self.tail.data

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        print("Deleted:", deleted)

    # 5. Insert after a given value
    def insert_after(self, given_data, data):
        current = self.head

        while current is not None:

            if current.data == given_data:
                newnode = Node(data)

                newnode.prev = current
                newnode.next = current.next

                if current.next is not None:
                    current.next.prev = newnode
                else:
                    self.tail = newnode

                current.next = newnode
                return

            current = current.next

        print("Element not found")

    # 6. Delete after a given value
    def delete_after(self, given_data):
        current = self.head

        while current is not None:

            if current.data == given_data:

                if current.next is None:
                    print("No node exists after this element")
                    return

                deleted = current.next
                current.next = deleted.next

                if deleted.next is not None:
                    deleted.next.prev = current
                else:
                    self.tail = current

                print("Deleted:", deleted.data)
                return

            current = current.next

        print("Element not found")

    # 7. Search an element
    def search(self, key):
        current = self.head
        position = 0

        while current is not None:

            if current.data == key:
                return position

            current = current.next
            position += 1

        return -1

    # 8. Forward traversal
    def display_forward(self):
        current = self.head

        if current is None:
            print("List is empty")
            return

        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next

        print("None")

    # 9. Backward traversal
    def display_backward(self):
        current = self.tail

        if current is None:
            print("List is empty")
            return

        while current is not None:
            print(current.data, end=" <-> ")
            current = current.prev

        print("None")


# Main program
dll = DoublyLinkedList()

while True:

    print("\n----- DOUBLY LINKED LIST -----")
    print("1. Insert at beginning")
    print("2. Insert at tail")
    print("3. Delete at beginning")
    print("4. Delete at tail")
    print("5. Insert after a value")
    print("6. Delete after a value")
    print("7. Search")
    print("8. Display forward")
    print("9. Display backward")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        dll.insert_at_beginning(value)

    elif choice == 2:
        value = int(input("Enter value: "))
        dll.insert_at_tail(value)

    elif choice == 3:
        dll.delete_at_beginning()

    elif choice == 4:
        dll.delete_at_tail()

    elif choice == 5:
        given = int(input("Insert after which value? "))
        value = int(input("Enter new value: "))
        dll.insert_after(given, value)

    elif choice == 6:
        given = int(input("Delete node after which value? "))
        dll.delete_after(given)

    elif choice == 7:
        value = int(input("Enter value to search: "))
        position = dll.search(value)

        if position == -1:
            print("Element not found")
        else:
            print("Element found at position:", position)

    elif choice == 8:
        dll.display_forward()

    elif choice == 9:
        dll.display_backward()

    elif choice == 10:
        print("Program exited")
        break

    else:
        print("Invalid choice")