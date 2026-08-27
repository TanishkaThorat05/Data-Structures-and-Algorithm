MAX_SIZE = 15
history = []


def visit_page(url):
    # Check HTTPS
    if not url.startswith("https://"):
        print("Error: Only HTTPS URLs are allowed.")
        return

    # Check consecutive duplicate
    if history and history[-1] == url:
        print("Page already visited consecutively. Duplicate not added.")
        return

    # Check maximum size
    if len(history) >= MAX_SIZE:
        print("Error: Browser history is full. New page rejected.")
        return

    history.append(url)
    print("Page visited:", url)


def go_back():
    if not history:
        print("History is empty. Cannot go back.")
        return

    removed = history.pop()
    print("Going back from:", removed)

    if history:
        print("Current page:", history[-1])
    else:
        print("No pages left in history.")


def current_page():
    if not history:
        print("History is empty.")
    else:
        print("Current page:", history[-1])


def display_history():
    if not history:
        print("Browser history is empty.")
        return

    print("\nBrowser History (latest first):")
    for i in range(len(history) - 1, -1, -1):
        print(history[i])


# Menu-driven program
while True:
    print("\n--- Browser History ---")
    print("1. Visit New Page (Push)")
    print("2. Go Back (Pop)")
    print("3. Current Page (Peek)")
    print("4. Display Browser History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        url = input("Enter URL: ")
        visit_page(url)

    elif choice == "2":
        go_back()

    elif choice == "3":
        current_page()

    elif choice == "4":
        display_history()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
