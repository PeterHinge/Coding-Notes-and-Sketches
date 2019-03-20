class MinHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0
        print("Initializing minimum heap...")

########################################################################################################################
    # Helpers:
    def get_parent_idx(self, idx):
        return idx // 2

    def get_left_child_idx(self, idx):
        return idx * 2

    def get_right_child_idx(self, idx):
        return idx * 2 + 1

    def has_child(self, idx):
        return self.get_left_child_idx(idx) <= self.count

########################################################################################################################

    def retrieve_min(self):
        if self.count == 0:
            print("No elements in heap.")
            return None

        minimum = self.heap_list[1]
        print("Removing {} from: {}".format(minimum, self.heap_list))
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        self.heap_list.pop()
        print("Last element moved to first: {}".format(self.heap_list))
        self.heapify_down()
        return minimum

    def add(self, element):
        self.count += 1
        print("Adding {} to: {}".format(element, self.heap_list))
        self.heap_list.append(element)
        self.heapify_up()

    def get_smaller_child_idx(self, idx):
        if self.get_right_child_idx(idx) > self.count:
            print("There is only a left child.")
            return self.get_left_child_idx(idx)
        else:
            left_child = self.heap_list[self.get_left_child_idx(idx)]
            right_child = self.heap_list[self.get_right_child_idx(idx)]
            if left_child < right_child:
                print("Left child is smaller.")
                return self.get_left_child_idx(idx)
            else:
                print("Right child is smaller.")
                return self.get_right_child_idx(idx)

    def heapify_up(self):
        idx = self.count
        while self.get_parent_idx(idx) > 0:
            if self.heap_list[self.get_parent_idx(idx)] > self.heap_list[idx]:
                tmp = self.heap_list[self.get_parent_idx(idx)]
                print("swapping {} with {}".format(tmp, self.heap_list[idx]))
                self.heap_list[self.get_parent_idx(idx)] = self.heap_list[idx]
                self.heap_list[idx] = tmp
            idx = self.get_parent_idx(idx)
        print("HEAP RESTORED! {}".format(self.heap_list))
        print("")

    def heapify_down(self):
        idx = 1
        while self.has_child(idx):
            smaller_child_idx = self.get_smaller_child_idx(idx)
            if self.heap_list[idx] > self.heap_list[smaller_child_idx]:
                tmp = self.heap_list[smaller_child_idx]
                print("swapping {} with {}".format(self.heap_list[idx], tmp))
                self.heap_list[smaller_child_idx] = self.heap_list[idx]
                self.heap_list[idx] = tmp
            idx = smaller_child_idx
        print("HEAP RESTORED! {}".format(self.heap_list))
        print("")


"""Example:
from random import randrange

min_heap = MinHeap()

random_nums = [randrange(1, 101) for n in range(15)]
for el in random_nums:
  min_heap.add(el)

while min_heap.count != 0:
  min_heap.retrieve_min()
"""
