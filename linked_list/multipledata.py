class Node:
    def __init__(self, name, usn, marks):
        self.data = {
            "name": name,
            "usn": usn,
            "marks": marks
        }

        self.prev = None
        self.next = None


# Create a student node
newnode = Node("Rahul", "4SM23CS001", 85)

# Display student details
print("Name:", newnode.data["name"])
print("USN:", newnode.data["usn"])
print("Marks:", newnode.data["marks"])