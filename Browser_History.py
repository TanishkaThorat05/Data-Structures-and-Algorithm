MAX_SIZE = 15
history = []


def visit_page(url):
    # Check URL
    if not url.startswith("https://"):
        print("Invalid URL! Only HTTPS URLs are allowed.")
        return

    # Check for consecutive duplicate
    if history and history[-1] == url:
        print("Page already at the top of history. No duplicate added.")
        return

    # Check if history is full
    if len(history) >= MAX_SIZE:
        print("Browser history is full. Cannot add new page.")
        return

    # Push URL onto stack
    history.append(url)
    print("Visited:", url)


def go_back():
    # Pop the current page
    if not history:
        print("History is empty. Cannot go back.")
        return

    page = history.pop()
    print("Going back from:", page)


def current_page():
    # Peek at the top of the stack
    if not history:
        print("No current page.")
    else:
        print("Current Page:", history[-1])


def display_history():
    if not history:
        print("Browser history is empty.")
        return

    print("\nBrowser History:")
    # Latest page is displayed first
    for i, url in enumerate(reversed(history), 1):
        print(f"{i}. {url}")


# Menu-driven program
while True:
    print("\n--- Browser History ---")
    print("1. Visit New Page")
    print("2. Go Back")
    print("3. Current Page")
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
        print("Invalid choice!")