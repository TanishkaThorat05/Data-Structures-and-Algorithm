# BST - Recursive Postorder Traversal

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert employee ID into BST
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


# Recursive Postorder Traversal
# Left -> Right -> Root
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Main program
root = None

print("Enter employee IDs (0 to stop):")

while True:
    id = int(input())

    if id == 0:
        break

    root = insert(root, id)


print("\nPostorder Traversal:")
postorder(root)