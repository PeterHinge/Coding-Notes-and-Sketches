class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
        print("Creating node with the value: {} and with a link to node: {}.".format(self.value, self.next_node))

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value


"""Example:
a = Node(1)
b = Node(2, a)

print(a.get_value())
print(b.get_next_node().get_value())
"""
