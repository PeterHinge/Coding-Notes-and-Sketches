class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        print("Creating node with the value: {}.".format(self.value))

    def add_child(self, child_node):
        if child_node in self.children:
            print("Child: {} already in parent: {}'s children.".format(str(child_node.value), str(self.value)))
            return
        self.children.append(child_node)
        print("Adding child: {} to parent: {}.".format(str(child_node.value), str(self.value)))

    def remove_child(self, child_node):
        if child_node not in self.children:
            print("Child: {} is not in parent: {}'s children.".format(str(child_node.value), str(self.value)))
            return
        self.children = [child for child in self.children if child is not child_node]
        print("Removing child: {} from parent: {}.".format(str(child_node.value), str(self.value)))

    def traverse(self):
        print("Traversing...")
        nodes_to_visit = [self]
        while len(nodes_to_visit) != 0:
            current_node = nodes_to_visit.pop()
            print(str(current_node.value))
            nodes_to_visit += current_node.children


"""Example:
root = TreeNode("root")
a = TreeNode("a")
b = TreeNode("b")
c = TreeNode("c")

a1 = TreeNode("a1")
a2 = TreeNode("a2")
b1 = TreeNode("b1")

root.add_child(a)
root.add_child(b)
root.add_child(c)

root.add_child(c)

a.add_child(a1)
a.add_child(a2)
b.add_child(b1)

root.traverse()

root.remove_child(a)
root.remove_child(b)
root.remove_child(c)

print(root.children)
"""
