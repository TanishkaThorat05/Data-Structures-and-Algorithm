MAX_SIZE = 50
patient_stack = []


def add_patient():
    # Check maximum stack size
    if len(patient_stack) >= MAX_SIZE:
        print("Stack is full. Cannot add more patient files.")
        return

    patient_id = input("Enter Patient ID: ").strip()

    # Check missing Patient ID
    if not patient_id:
        print("Patient ID cannot be empty.")
        return

    # Check unique Patient ID
    for patient in patient_stack:
        if patient["id"] == patient_id:
            print("Patient ID already exists. Duplicate IDs are not allowed.")
            return

    # Check patient type
    patient_type = input("Enter Patient Type (Emergency/Priority): ").strip().lower()

    if patient_type not in ["emergency", "priority"]:
        print("Only Emergency and Priority patients can be added.")
        return

    # Push patient file onto stack
    patient_stack.append({
        "id": patient_id,
        "type": patient_type.capitalize()
    })

    print("Patient file added successfully.")


def review_file():
    # Pop operation
    if not patient_stack:
        print("Stack is empty. No patient file to review.")
        return

    patient = patient_stack.pop()

    print("\nReviewing Patient File:")
    print("Patient ID:", patient["id"])
    print("Patient Type:", patient["type"])


def top_file():
    # Peek operation
    if not patient_stack:
        print("Stack is empty. No patient file available.")
        return

    patient = patient_stack[-1]

    print("\nTop Patient File:")
    print("Patient ID:", patient["id"])
    print("Patient Type:", patient["type"])


def display_stack():
    if not patient_stack:
        print("Patient file stack is empty.")
        return

    print("\n--- Patient File Stack ---")

    # Display from top to bottom
    for i, patient in enumerate(reversed(patient_stack), 1):
        print(
            f"{i}. Patient ID: {patient['id']} | "
            f"Type: {patient['type']}"
        )


# Menu-driven program
while True:
    print("\n===== Hospital Patient Files =====")
    print("1. Add Patient File")
    print("2. Review File")
    print("3. Top File")
    print("4. Display File Stack")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        review_file()

    elif choice == "3":
        top_file()

    elif choice == "4":
        display_stack()

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")