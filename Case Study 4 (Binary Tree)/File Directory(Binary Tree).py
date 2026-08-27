# Node class
class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


# Non-recursive Postorder Traversal using two stacks
def postorder_two_stacks(root):
    if root is None:
        print("Directory is empty.")
        return

    stack1 = []
    stack2 = []

    # Push root into Stack 1
    stack1.append(root)

    # Process Stack 1
    while stack1:
        current = stack1.pop()
        stack2.append(current)

        # Push left child into Stack 1
        if current.left:
            stack1.append(current.left)

        # Push right child into Stack 1
        if current.right:
            stack1.append(current.right)

    # Stack 2 contains nodes in postorder
    print("Postorder Traversal:")

    while stack2:
        current = stack2.pop()
        print(current.name, end=" ")


# Create file and folder tree
root = Node("Root")

root.left = Node("Documents")
root.right = Node("Pictures")

root.left.left = Node("Resume.pdf")
root.left.right = Node("Assignment.docx")

root.right.left = Node("Photo1.jpg")
root.right.right = Node("Photo2.jpg")


# Perform non-recursive postorder traversal
postorder_two_stacks(root)
