# Node class
class Node:
    def __init__(self, patient_id):
        self.patient_id = patient_id
        self.left = None
        self.right = None


# Binary Tree class
class BinaryTree:
    def __init__(self):
        self.root = None

    # Insert patient registration number
    def insert(self, patient_id):
        if self.root is None:
            self.root = Node(patient_id)
        else:
            self._insert(self.root, patient_id)

    def _insert(self, node, patient_id):
        if patient_id < node.patient_id:
            if node.left is None:
                node.left = Node(patient_id)
            else:
                self._insert(node.left, patient_id)

        else:
            if node.right is None:
                node.right = Node(patient_id)
            else:
                self._insert(node.right, patient_id)

    # Recursive Postorder Traversal
    def postorder(self, node):
        if node is not None:
            # Visit left subtree
            self.postorder(node.left)

            # Visit right subtree
            self.postorder(node.right)

            # Visit root
            print(node.patient_id, end=" ")


# Create binary tree
tree = BinaryTree()

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