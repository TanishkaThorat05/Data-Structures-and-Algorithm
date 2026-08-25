# Binary Search Tree (BST) - Recursive Traversals

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert a value into BST
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


# Inorder: Left -> Root -> Right
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Preorder: Root -> Left -> Right
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Postorder: Left -> Right -> Root
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Main program
root = None

print("Enter student roll numbers (0 to stop):")

while True:
    value = int(input())

    if value == 0:
        break

    root = insert(root, value)


print("\nInorder Traversal:")
inorder(root)

print("\nPreorder Traversal:")
preorder(root)

print("\nPostorder Traversal:")
postorder(root)