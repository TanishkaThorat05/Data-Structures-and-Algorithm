MAX_SIZE = 150

checkin_queue = []
boarding_pass_ids = set()


def add_passenger(pass_id, valid_ticket):
    # Check for empty Boarding Pass ID
    if not pass_id:
        print("Error: Boarding Pass ID is required.")
        return

    # Check valid ticket
    if valid_ticket.lower() != "yes":
        print("Error: Passenger does not have a valid ticket.")
        return

    # Check duplicate Boarding Pass ID
    if pass_id in boarding_pass_ids:
        print("Error: Duplicate Boarding Pass ID is not allowed.")
        return

    # Check queue capacity
    if len(checkin_queue) >= MAX_SIZE:
        print("Error: Check-in queue is full.")
        return

    # Add passenger to queue
    checkin_queue.append(pass_id)
    boarding_pass_ids.add(pass_id)

    print("Passenger added successfully:", pass_id)


def checkin_passenger():
    # Dequeue operation
    if not checkin_queue:
        print("Check-in queue is empty.")
        return

    pass_id = checkin_queue.pop(0)

    print("Checking in passenger:", pass_id)


def view_next_passenger():
    # Peek operation
    if not checkin_queue:
        print("Check-in queue is empty.")
        return

    print("Next passenger:", checkin_queue[0])


def display_queue():
    if not checkin_queue:
        print("Check-in queue is empty.")
        return

    print("\n--- Airport Check-in Queue ---")

    for i, pass_id in enumerate(checkin_queue, start=1):
        print(i, ".", pass_id)


# Menu-driven program
while True:
    print("\n===== Airport Check-in Queue =====")
    print("1. Add Passenger (Enqueue)")
    print("2. Check-in Passenger (Dequeue)")
    print("3. View Next Passenger")
    print("4. Display Check-in Queue")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        pass_id = input("Enter Boarding Pass ID: ")
        valid_ticket = input("Does the passenger have a valid ticket? (yes/no): ")

        add_passenger(pass_id, valid_ticket)

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

