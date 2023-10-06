class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if not self.is_empty():
            popped = self.top.data
            self.top = self.top.next
            self.size -= 1
            return popped

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if not self.is_empty():
            return self.top.data

    def get_size(self):
        return self.size
