# Node class
class Node:
    def __init__(self, employee_id):
        self.employee_id = employee_id
        self.left = None
        self.right = None


# Insert employee ID into BST
def insert(root, employee_id):
    if root is None:
        return Node(employee_id)

    if employee_id < root.employee_id:
        root.left = insert(root.left, employee_id)
    elif employee_id > root.employee_id:
        root.right = insert(root.right, employee_id)

    return root


# Recursive Postorder Traversal
# Left -> Right -> Root
def postorder(root):
    if root is not None:
        # Process left child
        postorder(root.left)

        # Process right child
        postorder(root.right)

        # Process parent
        print(root.employee_id, end=" ")


# Main program
root = None

print("Enter employee IDs (enter 0 to stop):")

while True:
    employee_id = int(input("Enter Employee ID: "))

    if employee_id == 0:
        break

    root = insert(root, employee_id)


# Display postorder traversal
print("\nPostorder Traversal:")
postorder(root)

print()
