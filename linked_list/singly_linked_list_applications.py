"""
BDE 5151 – Singly Linked List Applications (Assignment 1, Q2–Q10)
Run: python singly_linked_list_applications.py
"""

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def to_values(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.data)
            current = current.next
        return values

    # Q3: Sum of the last n nodes in one traversal.
    def sum_last_n(self, n):
        if n < 0:
            raise ValueError("n cannot be negative")
        if n == 0:
            return 0
        recent = deque()
        total = 0
        count = 0
        current = self.head
        while current is not None:
            recent.append(current.data)
            total += current.data
            count += 1
            if len(recent) > n:
                total -= recent.popleft()
            current = current.next
        if n > count:
            raise ValueError("n is greater than the number of nodes")
        return total

    # Q4: Reverse a singly linked list.
    def reverse(self):
        previous = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    # Q5: Split into two new lists containing alternate elements.
    def split_alternate(self):
        first = SinglyLinkedList()
        second = SinglyLinkedList()
        first_tail = None
        second_tail = None
        current = self.head
        index = 0
        while current is not None:
            new_node = Node(current.data)
            if index % 2 == 0:
                if first.head is None:
                    first.head = new_node
                else:
                    first_tail.next = new_node
                first_tail = new_node
            else:
                if second.head is None:
                    second.head = new_node
                else:
                    second_tail.next = new_node
                second_tail = new_node
            current = current.next
            index += 1
        return first, second

    # Helper used by Q6 to reverse a chain and return its new head.
    def reverse_chain(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous

    # Q6: Check palindrome and restore the original list.
    def is_palindrome(self):
        if self.head is None or self.head.next is None:
            return True
        slow = self.head
        fast = self.head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        second_half = self.reverse_chain(slow.next)
        slow.next = second_half
        left = self.head
        right = second_half
        result = True
        while right is not None:
            if left.data != right.data:
                result = False
                break
            left = left.next
            right = right.next
        slow.next = self.reverse_chain(second_half)
        return result

    # Q7: Remove duplicates, keeping the first occurrence.
    def remove_duplicates(self):
        seen = set()
        current = self.head
        previous = None
        while current is not None:
            if current.data in seen:
                previous.next = current.next
            else:
                seen.add(current.data)
                previous = current
            current = current.next

    # Q8: Find middle; for an even length, return the second middle.
    def find_middle(self):
        if self.head is None:
            return None
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.data


# Q2: Common elements. Input lists are individually unique as specified.
def common_elements(list1, list2):
    values_in_second = set(list2.to_values())
    result = SinglyLinkedList()
    current = list1.head
    while current is not None:
        if current.data in values_in_second:
            result.add_at_tail(current.data)
        current = current.next
    return result



# Q9: Circular singly linked list.
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def remove_odd_elements(self):
        if self.head is None:
            return
        count = 1
        tail = self.head
        while tail.next != self.head:
            tail = tail.next
            count += 1
        dummy = Node(None)
        dummy.next = self.head
        previous = dummy
        current = self.head
        kept_count = 0
        for _ in range(count):
            next_node = current.next
            if current.data % 2 != 0:
                previous.next = next_node
            else:
                previous = current
                kept_count += 1
            current = next_node
        if kept_count == 0:
            self.head = None
        else:
            self.head = dummy.next
            previous.next = self.head

    def display(self):
        if self.head is None:
            print("Circular list is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")


# Q10: Floyd's cycle detection algorithm.
def contains_cycle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


if __name__ == "__main__":
    print("\nQ2: COMMON ELEMENTS")
    a = SinglyLinkedList()
    b = SinglyLinkedList()
    for x in [10, 20, 30, 40]:
        a.add_at_tail(x)
    for x in [20, 40, 50, 60]:
        b.add_at_tail(x)
    common_elements(a, b).display()

    print("\nQ3: SUM OF LAST N")
    ll = SinglyLinkedList()
    for x in [10, 20, 30, 40, 50]:
        ll.add_at_tail(x)
    print("Sum of last 3:", ll.sum_last_n(3))

    print("\nQ4: REVERSE")
    ll.reverse()
    ll.display()

    print("\nQ5: SPLIT ALTERNATE")
    original = SinglyLinkedList()
    for x in [10, 20, 30, 40, 50, 60]:
        original.add_at_tail(x)
    first, second = original.split_alternate()
    print("First:")
    first.display()
    print("Second:")
    second.display()

    print("\nQ6: PALINDROME")
    p = SinglyLinkedList()
    for x in [10, 20, 30, 20, 10]:
        p.add_at_tail(x)
    print("Is palindrome?", p.is_palindrome())
    print("List restored:")
    p.display()

    print("\nQ7: REMOVE DUPLICATES")
    d = SinglyLinkedList()
    for x in [10, 20, 30, 20, 40, 10]:
        d.add_at_tail(x)
    d.remove_duplicates()
    d.display()

    print("\nQ8: MIDDLE ELEMENT")
    m = SinglyLinkedList()
    for x in [10, 20, 30, 40, 50]:
        m.add_at_tail(x)
    print("Middle:", m.find_middle())

    print("\nQ9: REMOVE ODD FROM CIRCULAR LIST")
    c = CircularSinglyLinkedList()
    for x in [1, 2, 3, 4, 5, 6]:
        c.add_at_tail(x)
    c.remove_odd_elements()
    c.display()

    print("\nQ10: CYCLE DETECTION")
    cycle = SinglyLinkedList()
    for x in [10, 20, 30, 40]:
        cycle.add_at_tail(x)
    print("Before cycle:", contains_cycle(cycle.head))
    last = cycle.head
    while last.next is not None:
        last = last.next
    last.next = cycle.head.next
    print("After creating cycle:", contains_cycle(cycle.head))
