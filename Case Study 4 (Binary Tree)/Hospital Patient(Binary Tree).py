# Node class
class Node:
    def __init__(self, registration_no):
        self.registration_no = registration_no
        self.left = None
        self.right = None


# Binary Tree class
class PatientTree:
    def __init__(self):
        self.root = None

    # Insert patient registration number
    def insert(self, registration_no):
        self.root = self.insert_recursive(self.root, registration_no)

    def insert_recursive(self, root, registration_no):
        if root is None:
            return Node(registration_no)

        if registration_no < root.registration_no:
            root.left = self.insert_recursive(root.left, registration_no)
        elif registration_no > root.registration_no:
            root.right = self.insert_recursive(root.right, registration_no)

        return root

    # Recursive Postorder Traversal
    def postorder(self, root):
        if root is not None:
            # Visit left subtree
            self.postorder(root.left)

            # Visit right subtree
            self.postorder(root.right)

            # Visit root
            print(root.registration_no, end=" ")


# Create patient binary tree
tree = PatientTree()

# Insert patient registration numbers
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(60)
tree.insert(80)

# Perform postorder traversal
print("Postorder Traversal:")
tree.postorder(tree.root)
