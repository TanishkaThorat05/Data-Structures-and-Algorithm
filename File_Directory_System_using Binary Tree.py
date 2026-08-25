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

    # Push root into first stack
    stack1.append(root)

    # Process nodes using two stacks
    while stack1:
        node = stack1.pop()
        stack2.append(node)

        # Push left child into stack1
        if node.left:
            stack1.append(node.left)

        # Push right child into stack1
        if node.right:
            stack1.append(node.right)

    # Print nodes from second stack
    print("Postorder Traversal:")

    while stack2:
        node = stack2.pop()
        print(node.name, end=" → ")


# Create file directory tree
root = Node("Root")

root.left = Node("Documents")
root.right = Node("Downloads")

root.left.left = Node("Assignments")
root.left.right = Node("Projects")

root.right.left = Node("Images")
root.right.right = Node("Videos")


# Perform postorder traversal
postorder_two_stacks(root)