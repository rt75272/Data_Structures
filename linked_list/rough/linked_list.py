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

    def insert_at_index(self, data, index):
        new_node = node.Node(data)
        current_node = self.head
        position = 0
        if(position == index):
            self.insert_at_start(data)
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
            if(current_node != None):
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    def insert_at_end(self, data):
        new_node = node.Node(data)
        if(self.head == None):
            self.head = new_node
        else:
            current_node = self.head
            while(current_node.next):
                current_node = current_node.next
            current_node.next = new_node

    def remove_first_node(self):
        if(self.head == None):
            return
        else:
            self.head = self.head.next

    def get_size(self):
        size = 0 
        if(self.head):
            current_node = self.head
            while(current_node):
                size+=1
                current_node = current_node.next
            return size
        else:
            return 0

    def print_list(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next
