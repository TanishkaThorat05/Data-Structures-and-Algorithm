MAX_SIZE = 100
patient_queue = []
registered_patients = set()


def register_patient():
    # Check if queue is full
    if len(patient_queue) >= MAX_SIZE:
        print("Queue is full. No new patient can join.")
        return

    patient_id = input("Enter Patient ID: ").strip()

    # Check missing Patient ID
    if not patient_id:
        print("Patient ID cannot be empty.")
        return

    # Check duplicate Patient ID
    if patient_id in registered_patients:
        print("Patient ID already exists. Duplicate IDs are not allowed.")
        return

    # Register patient
    registered_patients.add(patient_id)

    # Enqueue patient
    patient_queue.append(patient_id)

    print("Patient registered and added to the queue.")


def call_patient():
    # Check if queue is empty
    if not patient_queue:
        print("Queue is empty. No patient to call.")
        return

    # Dequeue the first patient
    patient_id = patient_queue.pop(0)

    print("Calling Patient:", patient_id)


def view_next_patient():
    # Peek operation
    if not patient_queue:
        print("Queue is empty. No patient waiting.")
        return

    print("Next Patient:", patient_queue[0])


def display_queue():
    if not patient_queue:
        print("Patient queue is empty.")
        return

    print("\n--- Patient Queue ---")

    # Display from first to last
    for i, patient_id in enumerate(patient_queue, 1):
        print(f"{i}. Patient ID: {patient_id}")


# Menu-driven program
while True:
    print("\n===== Hospital Patient Queue =====")
    print("1. Register Patient")
    print("2. Call Patient")
    print("3. View Next Patient")
    print("4. Display Patient Queue")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_patient()

    elif choice == "2":
        call_patient()

    elif choice == "3":
        view_next_patient()

    elif choice == "4":
        display_queue()

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
