class Node:
    def __init__(self, book):
        self.book = book
        self.next = None


class LibraryCatalog:
    def __init__(self):
        self.head = None

    # Insert a book at the beginning
    def insert_beginning(self, book):
        new_node = Node(book)
        new_node.next = self.head
        self.head = new_node
        print(f"'{book}' inserted at the beginning.")

    # Insert a book at the end
    def insert_end(self, book):
        new_node = Node(book)

        if self.head is None:
            self.head = new_node
            print(f"'{book}' inserted at the end.")
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node
        print(f"'{book}' inserted at the end.")

    # Delete a book from the beginning
    def delete_beginning(self):
        if self.head is None:
            print("Library catalog is empty.")
            return

        deleted_book = self.head.book
        self.head = self.head.next
        print(f"'{deleted_book}' deleted from the beginning.")

    # Display all books
    def display(self):
        if self.head is None:
            print("Library catalog is empty.")
            return

        current = self.head
        print("Library Catalog:")

        while current is not None:
            print(current.book)
            current = current.next


# Example usage
library = LibraryCatalog()

library.insert_beginning("Python Programming")
library.insert_beginning("Data Structures")
library.insert_end("Computer Networks")
library.insert_end("Database Management")

print("\nAfter insertion:")
library.display()

print("\nDeleting from beginning:")
library.delete_beginning()

print("\nAfter deletion:")
library.display()
