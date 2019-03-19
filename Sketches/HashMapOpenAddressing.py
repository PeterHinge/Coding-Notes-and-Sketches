class HashMapOA:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for i in range(array_size)]
        print(("Creating a hash map with the array size of {}.".format(str(self.array_size))))

    def hash(self, key, count_collisions=0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        if current_array_value is None:
            self.array[array_index] = [key, value]
            print("Assigning key: {} and value: {} to the hash map at index {}.".format(str(key), str(value),
                                                                                        str(array_index)))
            return

        if current_array_value[0] == key:
            print("Key already exists! Overwriting key: {} and changing its value to: {} "
                  "in the hash map at index {}.".format(str(key), str(value), str(array_index)))
            self.array[array_index] = [key, value]
            return

    # Collision!
        number_collisions = 1

        while current_array_value[0] != key:
            print("{} collisions found!".format(str(number_collisions)))
            new_hash_code = self.hash(key, number_collisions)
            new_array_index = self.compressor(new_hash_code)
            current_array_value = self.array[new_array_index]

            if current_array_value is None:
                self.array[new_array_index] = [key, value]
                print("Assigning key: {} and value: {} to the hash map at index {}.".format(str(key), str(value),
                                                                                            str(new_array_index)))
                return

            if current_array_value[0] == key:
                print("Key already exists! Overwriting key: {} and changing its value to: {} "
                      "in the hash map at index {}.".format(str(key), str(value), str(new_array_index)))
                self.array[new_array_index] = [key, value]
                return

            number_collisions += 1
        return

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]
        print("Attempting to retrieve key: {}'s value.".format(str(key)))

        if possible_return_value is None:
            print("No value found with key: {}.".format(str(key)))
            return None

        if possible_return_value[0] == key:
            print("Value: {} found in hash map at index {} with key: {}.".format(str(possible_return_value[1]),
                                                                                 str(array_index), str(key)))
            return possible_return_value[1]

    # Collision!
        retrieval_collisions = 1

        while possible_return_value != key:
            print("{} collisions found!".format(str(retrieval_collisions)))
            new_hash_code = self.hash(key, retrieval_collisions)
            retrieving_array_index = self.compressor(new_hash_code)
            possible_return_value = self.array[retrieving_array_index]

            if possible_return_value is None:
                print("No value found with key: {}.".format(str(key)))
                return None

            if possible_return_value[0] == key:
                print("Value: {} found in hash map at index {} with key: {}.".format(str(possible_return_value[1]),
                                                                                     str(retrieving_array_index),
                                                                                     str(key)))
                return possible_return_value[1]

            retrieval_collisions += 1

        return


"""Example:
hash_map = HashMapOA(3)

hash_map.assign('key1', 'value1')
hash_map.assign('key2', 'value3')
hash_map.assign('key2', 'value2')

hash_map.retrieve('key3')

hash_map.retrieve('key2')
"""
