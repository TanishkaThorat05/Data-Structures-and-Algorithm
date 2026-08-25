# Node class
class Node:
    def __init__(self, patient_id):
        self.patient_id = patient_id
        self.next = None


# Linked List class
class PatientList:
    def __init__(self):
        self.head = None

    # Add patient to the end
    def add_patient(self, patient_id):
        new_node = Node(patient_id)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    # Delete patient
    def delete_patient(self, patient_id):
        if self.head is None:
            print("Patient list is empty.")
            return

        # If the patient is the first node
        if self.head.patient_id == patient_id:
            self.head = self.head.next
            print(patient_id, "deleted successfully.")
            return

        current = self.head

        # Search for the patient
        while current.next:
            if current.next.patient_id == patient_id:
                current.next = current.next.next
                print(patient_id, "deleted successfully.")
                return

            current = current.next

        # Patient not found
        print(patient_id, "not found in the patient list.")

    # Display patient list
    def display(self):
        if self.head is None:
            print("Patient list is empty.")
            return

        current = self.head

        while current:
            print(current.patient_id, end="")

            if current.next:
                print(" → ", end="")

            current = current.next

        print()


# Create patient list
patients = PatientList()

# Add patients
patients.add_patient("P101")
patients.add_patient("P102")
patients.add_patient("P103")
patients.add_patient("P104")


# 1. Display current patient list
print("1. Current Patient List:")
patients.display()


# 2. Delete P103
print("\n2. Deleting P103:")
patients.delete_patient("P103")


# 3. Display list after deletion
print("\n3. Patient List After Deletion:")
patients.display()


# 4. Try to delete P110
print("\n4. Deleting P110:")
patients.delete_patient("P110")