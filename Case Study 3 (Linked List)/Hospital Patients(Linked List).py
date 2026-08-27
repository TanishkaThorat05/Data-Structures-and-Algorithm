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

    # Display patient list
    def display(self):
        if self.head is None:
            print("Patient list is empty.")
            return

        current = self.head

        while current:
            print(current.patient_id, end="")
            if current.next:
                print(" -> ", end="")
            current = current.next

        print()

    # Delete patient
    def delete_patient(self, patient_id):
        if self.head is None:
            print("Patient list is empty.")
            return

        # If patient is the first node
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


# Create patient list
patients = PatientList()

# Current list
patients.add_patient("P101")
patients.add_patient("P102")
patients.add_patient("P103")
patients.add_patient("P104")

# Display current list
print("Current Patient List:")
patients.display()

# Delete P103
print("\nDeleting P103:")
patients.delete_patient("P103")

# Display list after deletion
print("\nPatient List After Deletion:")
patients.display()

# Try to delete P110
print("\nDeleting P110:")
patients.delete_patient("P110")
