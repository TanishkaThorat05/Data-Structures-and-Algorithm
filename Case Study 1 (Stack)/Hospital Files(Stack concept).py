MAX_SIZE = 50
patient_stack = []


def add_patient(patient_id, priority):
    # Check for missing Patient ID
    if not patient_id:
        print("Error: Patient ID is required.")
        return

    # Check priority type
    if priority not in ["Emergency", "Priority"]:
        print("Error: Only Emergency and Priority patients are allowed.")
        return

    # Check maximum size
    if len(patient_stack) >= MAX_SIZE:
        print("Error: Patient file stack is full.")
        return

    # Check unique Patient ID
    for patient in patient_stack:
        if patient["id"] == patient_id:
            print("Error: Patient ID already exists.")
            return

    # Push patient file onto stack
    patient_stack.append({
        "id": patient_id,
        "priority": priority
    })

    print("Patient file added successfully.")


def review_file():
    # Pop operation
    if not patient_stack:
        print("Patient file stack is empty.")
        return

    patient = patient_stack.pop()

    print("\nReviewing Patient File:")
    print("Patient ID:", patient["id"])
    print("Priority:", patient["priority"])


def top_file():
    # Peek operation
    if not patient_stack:
        print("Patient file stack is empty.")
        return

    patient = patient_stack[-1]

    print("\nTop Patient File:")
    print("Patient ID:", patient["id"])
    print("Priority:", patient["priority"])


def display_stack():
    if not patient_stack:
        print("Patient file stack is empty.")
        return

    print("\n--- Patient File Stack ---")

    # Display from top to bottom
    for i in range(len(patient_stack) - 1, -1, -1):
        patient = patient_stack[i]
        print(
            "Patient ID:", patient["id"],
            "| Type:", patient["priority"]
        )


# Menu-driven program
while True:
    print("\n===== Hospital Patient Files =====")
    print("1. Add Patient File (Push)")
    print("2. Review File (Pop)")
    print("3. Top File (Peek)")
    print("4. Display File Stack")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        patient_id = input("Enter Patient ID: ")
        priority = input("Enter Patient Type (Emergency/Priority): ")

        add_patient(patient_id, priority)

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
