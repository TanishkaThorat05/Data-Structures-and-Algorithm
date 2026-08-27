# Node class
class Node:
    def __init__(self, system_id):
        self.system_id = system_id
        self.next = None


# Linked List class
class SystemList:
    def __init__(self):
        self.head = None

    # Insert system at the end
    def insert(self, system_id):
        new_node = Node(system_id)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    # Delete a system
    def delete(self, system_id):
        if self.head is None:
            print("System list is empty.")
            return

        # If deleting the first node
        if self.head.system_id == system_id:
            self.head = self.head.next
            print(system_id, "deleted successfully.")
            return

        current = self.head

        while current.next:
            if current.next.system_id == system_id:
                current.next = current.next.next
                print(system_id, "deleted successfully.")
                return

            current = current.next

        # System not found
        print(system_id, "not found in the system list.")

    # Display linked list
    def display(self):
        if self.head is None:
            print("System list is empty.")
            return

        current = self.head

        while current:
            print(current.system_id, end="")

            if current.next:
                print(" -> ", end="")

            current = current.next

        print()


# Create linked list
systems = SystemList()

# Add initial systems
systems.insert("PC1")
systems.insert("PC2")
systems.insert("PC3")
systems.insert("PC4")
systems.insert("PC5")

# Display all systems
print("All Computer Lab Systems:")
systems.display()

# Delete PC3
print("\nDeleting PC3:")
systems.delete("PC3")

# Insert PC6
print("\nInserting PC6:")
systems.insert("PC6")

# Display updated list
print("\nUpdated Computer Lab Systems:")
systems.display()

# Try to delete PC10
print("\nDeleting PC10:")
systems.delete("PC10")
