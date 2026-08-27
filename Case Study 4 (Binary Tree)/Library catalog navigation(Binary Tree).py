class Node:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None


class LibraryCatalog:
    def __init__(self):
        self.root = None

    # Insert a book into the Binary Search Tree
    def insert(self, book):
        new_node = Node(book)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if book < current.book:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right

    # Inorder Traversal
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.book)
            self.inorder(node.right)

    # Preorder Traversal
    def preorder(self, node):
        if node is not None:
            print(node.book)
            self.preorder(node.left)
            self.preorder(node.right)

    # Postorder Traversal
    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.book)


# Example usage
library = LibraryCatalog()

library.insert("Python Programming")
library.insert("Data Structures")
library.insert("Computer Networks")
library.insert("Database Management")
library.insert("Operating Systems")

print("Inorder Traversal:")
library.inorder(library.root)

print("\nPreorder Traversal:")
library.preorder(library.root)

print("\nPostorder Traversal:")
library.postorder(library.root)
