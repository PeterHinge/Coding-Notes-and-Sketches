from Node import Node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)
        print("Creating a linked list with the head node value of {}.".format(str(value)))

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
        print("Inserting {} as the beginning of the linked list".format(str(new_node.get_value())))

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
            print("Removing {} from the linked list.".format(str(current_node.get_value())))
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    print("Removing {} from the linked list.".format(str(next_node.get_value())))
                    current_node = None
                else:
                    current_node = next_node


"""Example:
ll = LinkedList(1)

ll.insert_beginning(2)
ll.insert_beginning(3)
ll.insert_beginning(4)
print(ll.stringify_list())

ll.remove_node(4)
print(ll.stringify_list())

ll.remove_node(2)
print(ll.stringify_list())
"""
