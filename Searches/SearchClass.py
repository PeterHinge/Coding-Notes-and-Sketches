class Search:
    def __init__(self, input_list, target_value=None):
        self.input_list = input_list
        self.target_value = target_value
        if len(self.input_list) <= 0:
            print("No values in list!")
        if not self.target_value:
            print("There is no target value!")

    def sort(self):
        return self.input_list.sort

    def linear(self):
        for index in range(len(self.input_list)):
            if self.input_list[index] == self.target_value:
                return print("{} found at index {}.".format(self.target_value, index))
        return print("{} not found in list.".format(self.target_value))

    def binary(self):
        try:

            current_list = self.input_list
            index_of_value = 0
            depth_counter = 0

            while True:
                mid_index = len(current_list) // 2
                mid_value = current_list[mid_index]

                if mid_value == self.target_value:
                    index_of_value += mid_index
                    depth_counter += 1
                    return print("Value {} found at index {}, with a search depth of {}.".format(
                        self.target_value, index_of_value, depth_counter))

                elif mid_value > self.target_value:
                    current_list = current_list[:mid_index]
                    depth_counter += 1
                    continue

                elif mid_value < self.target_value:
                    current_list = current_list[mid_index + 1:current_list[-1]]
                    index_of_value += mid_index + 1
                    depth_counter += 1
                    continue

                else:
                    print("Something went wrong!")
                    break

        # Error handling:
        except ValueError:
            print("{} not found in list.".format(self.target_value))
        except IndexError:
            print("{} not found in list.".format(self.target_value))
        except TypeError:
            print("TypeError: slice indices must be integers or None.")
