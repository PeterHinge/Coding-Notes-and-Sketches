from Node import Node


class Stack:
    def __init__(self, size_limit=None):
        self.size_limit = size_limit
        self.size = 0
        self.top_item = None
        print("Creating a stack with the size limit value of {}.".format(str(self.size_limit)))

    def push(self, value):
        if self.has_space():
            item_to_push = Node(value)
            item_to_push.set_next_node(self.top_item)
            self.top_item = item_to_push
            self.size += 1
            print("Pushing {} to the stack.".format(str(value)))
        else:
            print("No room for {} in stack.".format(str(value)))

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            print("Popping {} from the stack.".format(str(item_to_remove.get_value())))
            return item_to_remove.get_value()
        print("Stack is empty.")

    def peek(self):
        if not self.is_empty():
            return print(self.top_item.get_value())
        print("Stack is empty.")

    def has_space(self):
        return self.size_limit > self.size

    def is_empty(self):
        return self.size == 0


"""Example:
s = Stack(3)

s.peek()

s.push(1)
s.push(2)
s.push(3)

s.push(4)
s.peek()

s.pop()
s.pop()
s.pop()
s.pop()
"""
