
# Priority queue implementation in Python using a binary heap.
# The heap is stored in an array and automatically balanced.
# Pop is O(logn)


class MinPriorityQueue(object):

    def __init__(self):

        # Each node is a tuple of (value, priority, insert_counter)
        self.nodes = [None]

        # Current state of the insert counter, used when the priorities are same
        self.insert_counter = 0

    # Comparison function between two nodes
    # Higher priority wins
    # On equal priority: Lower insert counter wins
    @staticmethod
    def _is_lower_than(a, b):
        return b[1] > a[1] or (a[1] == b[1] and a[2] > b[2])

    # checks if the queue is empty
    def empty(self):
        return True if len(self.nodes) == 1 else False

    # Move a node up until the parent is bigger
    def _heapify(self, new_node_index):
        while 1 < new_node_index:
            new_node = self.nodes[new_node_index]
            parent_index = new_node_index // 2
            parent_node = self.nodes[parent_index]

            # Parent too big?
            if self._is_lower_than(parent_node, new_node):
                break

            # Swap with parent
            tmp_node = parent_node
            self.nodes[parent_index] = new_node
            self.nodes[new_node_index] = tmp_node

            # Continue further up
            new_node_index = parent_index

    # Add a new node with a given priority
    def add(self, value, priority):
        new_node_index = len(self.nodes)
        self.insert_counter += 1
        self.nodes.append(tuple((value, priority, self.insert_counter)))

        # Move the new node up in the hierarchy
        self._heapify(new_node_index)

    # Remove the top element and return it
    def remove(self):

        if len(self.nodes) == 1:
            raise LookupError("Heap is empty")

        result = self.nodes[1]

        # Move empty space down
        empty_space_index = 1
        while empty_space_index * 2 < len(self.nodes):

            left_child_index = empty_space_index * 2
            right_child_index = empty_space_index * 2 + 1

            # Left child wins
            if (
                len(self.nodes) <= right_child_index
                or self._is_lower_than(self.nodes[left_child_index], self.nodes[right_child_index])
            ):
                self.nodes[empty_space_index] = self.nodes[left_child_index]
                empty_space_index = left_child_index

            # Right child wins
            else:
                self.nodes[empty_space_index] = self.nodes[right_child_index]
                empty_space_index = right_child_index

        # Swap empty space with the last element and heapify
        last_node_index = len(self.nodes) - 1
        self.nodes[empty_space_index] = self.nodes[last_node_index]
        self._heapify(empty_space_index)

        # Throw out the last element
        self.nodes.pop()

        return result[0], result[1]
