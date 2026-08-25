MAX_SIZE = 150
passenger_queue = []
valid_tickets = set()


def add_passenger():
    # Check queue capacity
    if len(passenger_queue) >= MAX_SIZE:
        print("Queue is full. Cannot add more passengers.")
        return

    boarding_id = input("Enter Boarding Pass ID: ").strip()

    # Check missing Boarding Pass ID
    if not boarding_id:
        print("Boarding Pass ID cannot be empty.")
        return

    # Check duplicate Boarding Pass ID
    if boarding_id in valid_tickets:
        print("Boarding Pass ID already exists.")
        return

    # Check ticket validity
    ticket = input("Enter Ticket Number: ").strip()

    if not ticket:
        print("Invalid ticket. Passenger cannot be added.")
        return

    # Store valid ticket/boarding ID
    valid_tickets.add(boarding_id)

    # Enqueue passenger
    passenger_queue.append({
        "boarding_id": boarding_id,
        "ticket": ticket
    })

    print("Passenger added to the check-in queue successfully.")


def checkin_passenger():
    # Check if queue is empty
    if not passenger_queue:
        print("Queue is empty. No passenger to check in.")
        return

    # Dequeue the first passenger
    passenger = passenger_queue.pop(0)

    print("\nChecking in passenger:")
    print("Boarding Pass ID:", passenger["boarding_id"])
    print("Ticket Number:", passenger["ticket"])


def view_next_passenger():
    # Peek operation
    if not passenger_queue:
        print("Queue is empty. No passenger waiting.")
        return

    passenger = passenger_queue[0]

    print("\nNext Passenger:")
    print("Boarding Pass ID:", passenger["boarding_id"])
    print("Ticket Number:", passenger["ticket"])


def display_queue():
    if not passenger_queue:
        print("Check-in queue is empty.")
        return

    print("\n--- Airport Check-in Queue ---")

    for i, passenger in enumerate(passenger_queue, 1):
        print(
            f"{i}. Boarding Pass ID: {passenger['boarding_id']} | "
            f"Ticket: {passenger['ticket']}"
        )


# Menu-driven program
while True:
    print("\n===== Airport Check-in Queue =====")
    print("1. Add Passenger")
    print("2. Check-in Passenger")
    print("3. View Next Passenger")
    print("4. Display Check-in Queue")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_passenger()

    elif choice == "2":
        checkin_passenger()

    elif choice == "3":
        view_next_passenger()

    elif choice == "4":
        display_queue()

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")