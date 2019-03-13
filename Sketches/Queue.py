from Node import Node


class Queue:
    def __init__(self, size_limit=None):
        self.size_limit = size_limit
        self.size = 0
        self.head = None
        self.tail = None
        print("Creating a queue with the size limit value of {}.".format(str(self.size_limit)))

    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            print("Adding {} to the queue.".format(str(item_to_add.get_value())))
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("No room for {} in queue.".format(value))

    def dequeue(self):
        if self.get_size() > 0:
            item_to_remove = self.head
            print("Removing {} from the queue.".format(str(item_to_remove.get_value())))
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("Queue is empty.")

    def peek(self):
        if self.size > 0:
            return print(self.head.get_value())
        else:
            print("Queue is empty.")

    def get_size(self):
        return self.size

    def has_space(self):
        if self.size_limit is None:
            return True
        else:
            return self.size_limit > self.get_size()

    def is_empty(self):
        return self.size == 0


"""Example:
q = Queue(3)

q.peek()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

q.peek()

q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
"""
