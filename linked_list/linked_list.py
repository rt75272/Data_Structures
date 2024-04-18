import node

class LinkedList:
    # Constructor function
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = node.Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
        
    def remove_first_node(self):
        if(self.head == None):
            return
        else:
            self.head = self.head.next

    def print_list(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next
