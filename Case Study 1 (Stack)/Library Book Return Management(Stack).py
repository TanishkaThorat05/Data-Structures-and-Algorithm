class BookReturnStack:
    def __init__(self):
        self.stack = []

    # Add a returned book to the stack
    def push(self, book):
        self.stack.append(book)
        print(f"Book returned: {book}")

    # Remove the most recently returned book
    def pop(self):
        if self.is_empty():
            print("No books to process.")
            return None

        book = self.stack.pop()
        print(f"Processing book: {book}")
        return book

    # View the most recently returned book
    def peek(self):
        if self.is_empty():
            print("No returned books.")
        else:
            print(f"Latest returned book: {self.stack[-1]}")

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Display all returned books
    def display(self):
        if self.is_empty():
            print("No returned books.")
        else:
            print("Returned books (top to bottom):")
            for book in reversed(self.stack):
                print(book)


# Example usage
books = BookReturnStack()

books.push("Python Programming")
books.push("Data Structures")
books.push("Computer Networks")

books.display()

print("\nLatest returned book:")
books.peek()

print("\nProcessing returns:")
books.pop()
books.pop()

print("\nRemaining books:")
books.display()
