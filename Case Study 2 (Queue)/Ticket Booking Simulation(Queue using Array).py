class TicketQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.front = 0
        self.rear = -1
        self.count = 0

    # Add a customer to the queue
    def enqueue(self, customer):
        if self.count == self.size:
            print("Queue is full. Cannot add customer.")
            return

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = customer
        self.count += 1
        print(f"{customer} joined the ticket queue.")

    # Serve the customer at the front
    def dequeue(self):
        if self.count == 0:
            print("Queue is empty. No customers to serve.")
            return

        customer = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1

        print(f"{customer} got the ticket.")
        return customer

    # Display the queue
    def display(self):
        if self.count == 0:
            print("Queue is empty.")
            return

        print("Customers waiting in queue:")
        index = self.front

        for i in range(self.count):
            print(self.queue[index])
            index = (index + 1) % self.size


# Example usage
ticket_queue = TicketQueue(5)

ticket_queue.enqueue("Customer 1")
ticket_queue.enqueue("Customer 2")
ticket_queue.enqueue("Customer 3")
ticket_queue.enqueue("Customer 4")

print("\nCurrent Queue:")
ticket_queue.display()

print("\nServing Customers:")
ticket_queue.dequeue()
ticket_queue.dequeue()

print("\nRemaining Queue:")
ticket_queue.display()
