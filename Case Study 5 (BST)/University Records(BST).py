# Node class
class Node:
    def __init__(self, roll_no):
        self.roll_no = roll_no
        self.left = None
        self.right = None


# Insert a roll number into BST
def insert(root, roll_no):
    if root is None:
        return Node(roll_no)

    if roll_no < root.roll_no:
        root.left = insert(root.left, roll_no)
    elif roll_no > root.roll_no:
        root.right = insert(root.right, roll_no)

    return root


# Inorder: Left -> Root -> Right
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.roll_no, end=" ")
        inorder(root.right)


# Preorder: Root -> Left -> Right
def preorder(root):
    if root is not None:
        print(root.roll_no, end=" ")
        preorder(root.left)
        preorder(root.right)


# Postorder: Left -> Right -> Root
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.roll_no, end=" ")


# Main program
root = None

print("Enter student roll numbers (enter 0 to stop):")

while True:
    roll_no = int(input("Enter roll number: "))

    if roll_no == 0:
        break

    root = insert(root, roll_no)


# Display traversals
print("\nInorder Traversal:")
inorder(root)

print("\n\nPreorder Traversal:")
preorder(root)

print("\n\nPostorder Traversal:")
postorder(root)

print()
