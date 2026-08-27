MAX_SIZE = 100

patient_queue = []
registered_patients = set()


def register_patient(patient_id):
    # Check for empty Patient ID
    if not patient_id:
        print("Error: Patient ID is required.")
        return

    # Check duplicate Patient ID
    if patient_id in registered_patients:
        print("Error: Patient ID already registered.")
        return

    # Check queue capacity
    if len(patient_queue) >= MAX_SIZE:
        print("Error: Queue is full. Cannot add new patient.")
        return

    # Register and enqueue patient
    registered_patients.add(patient_id)
    patient_queue.append(patient_id)

    print("Patient registered and added to queue:", patient_id)


def call_patient():
    # Dequeue operation
    if not patient_queue:
        print("Queue is empty. No patient to call.")
        return

    patient_id = patient_queue.pop(0)

    print("Calling patient:", patient_id)


def view_next_patient():
    # Peek operation
    if not patient_queue:
        print("Queue is empty.")
        return

    print("Next patient:", patient_queue[0])


def display_queue():
    if not patient_queue:
        print("Patient queue is empty.")
        return

    print("\n--- Patient Queue ---")

    for i, patient_id in enumerate(patient_queue, start=1):
        print(i, ".", patient_id)


# Menu-driven program
while True:
    print("\n===== Hospital Patient Queue =====")
    print("1. Register Patient (Enqueue)")
    print("2. Call Patient (Dequeue)")
    print("3. View Next Patient")
    print("4. Display Patient Queue")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        patient_id = input("Enter Patient ID: ")
        register_patient(patient_id)

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
