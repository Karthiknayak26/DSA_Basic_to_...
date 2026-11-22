class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Check whether Queue is empty
    def is_empty(self):
        return self.front == -1

    # Check whether Queue is full
    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    # Insert an element
    def enqueue(self, data):
        if self.is_full():
            print("Circular Queue is full")

        else:
            if self.front == -1:
                self.front = 0
                self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.size

            self.queue[self.rear] = data
            print("Inserted:", data)

    # Delete an element
    def dequeue(self):
        if self.is_empty():
            print("Circular Queue is empty")

        else:
            deleted = self.queue[self.front]
            self.queue[self.front] = None

            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % self.size

            print("Deleted:", deleted)

    # Display front element
    def peek(self):
        if self.is_empty():
            print("Circular Queue is empty")
        else:
            print("Front element:", self.queue[self.front])

    # Display rear element
    def rear_element(self):
        if self.is_empty():
            print("Circular Queue is empty")
        else:
            print("Rear element:", self.queue[self.rear])

    # Display all elements
    def display(self):
        if self.is_empty():
            print("Circular Queue is empty")
            return

        print("Queue elements:", end=" ")

        i = self.front

        while True:
            print(self.queue[i], end=" ")

            if i == self.rear:
                break

            i = (i + 1) % self.size

        print()


# Main program
size = int(input("Enter Circular Queue size: "))

if size <= 0:
    print("Queue size must be positive")

else:
    q = CircularQueue(size)

    while True:
        print("\n--- CIRCULAR QUEUE MENU ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Rear Element")
        print("5. Display")
        print("6. Check Empty")
        print("7. Check Full")
        print("8. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter element: "))
            q.enqueue(data)

        elif choice == 2:
            q.dequeue()

        elif choice == 3:
            q.peek()

        elif choice == 4:
            q.rear_element()

        elif choice == 5:
            q.display()

        elif choice == 6:
            print("Is Empty:", q.is_empty())

        elif choice == 7:
            print("Is Full:", q.is_full())

        elif choice == 8:
            print("Exiting...")
            break

        else:
            print("Invalid choice")