class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_end(self, new_value):
        self.length += 1
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            previous_node = self.tail
            previous_node.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

    def get_node(self, index):
        current_node = self.head
        count = 0
        while current_node is not None:
            if count == index:
                return current_node
            current_node = current_node.next
            count += 1
        else:
            raise IndexError("list index out of range")

    def __str__(self):
        if self.head is not None:
            current = self.head
            out = 'LinkedList [' + str(current.value) + ', '
            while current.next is not None:
                current = current.next
                out += str(current.value) + ', '
            return out + ']'
        return 'LinkedList []'