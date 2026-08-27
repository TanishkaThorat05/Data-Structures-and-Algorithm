class Node:
    def __init__(self, admission_no, name):
        self.admission_no = admission_no
        self.name = name
        self.left = None
        self.right = None


class StudentBST:
    def __init__(self):
        self.root = None

    # Insert a student
    def insert(self, admission_no, name):
        new_node = Node(admission_no, name)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if admission_no < current.admission_no:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left

            elif admission_no > current.admission_no:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

            else:
                print("Admission number already exists.")
                return

    # Search for a student
    def search(self, admission_no):
        current = self.root

        while current is not None:
            if admission_no == current.admission_no:
                print("Student Found:")
                print("Admission No:", current.admission_no)
                print("Name:", current.name)
                return

            elif admission_no < current.admission_no:
                current = current.left

            else:
                current = current.right

        print("Student not found.")

    # Display students in ascending admission number
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.admission_no, "-", node.name)
            self.inorder(node.right)


# Example usage
students = StudentBST()

students.insert(105, "Rahul")
students.insert(102, "Priya")
students.insert(110, "Amit")
students.insert(101, "Sneha")
students.insert(108, "Kiran")

print("Student Admission Records:")
students.inorder(students.root)

print("\nSearching for Admission No. 108:")
students.search(108)

print("\nSearching for Admission No. 115:")
students.search(115)
