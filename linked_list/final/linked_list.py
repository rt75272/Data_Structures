import node

class LinkedList:
    # Constructor
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = node.Node(data)
        if(self.head == None):
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_index(self, data, index):
        new_node = node.Node(data)
        position = 0
        current_node = self.head
        if(position == index):
            self.insert_at_start(data)
        else:
            while(current_node != None and position+1 != index):
                position+=1
                current_node = current_node.next
            if(current_node != None):
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not found")

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

    def remove_last_node(self):
        # Check for empty list
        if(self.head == None):
            return
        
        current_node = self.head
        while(current_node.next.next):
            current_node = current_node.next
        current_node.next = None
    
    def remove_at_index(self, index):
        # Check for empty list
        if(self.head == None):
            return
        
        current_node = self.head
        position = 0 
        
        # Check for first node.
        if(position == index):
            self.remove_first_node()
        else:
            # Shifting to index node.
            while(current_node != None and position+1 != index):
                position+=1
                current_node = current_node.next
            # Remove pointer to index node.
            if(current_node != None):
                current_node.next = current_node.next.next
            else:
                print("Index not found")
        
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
    

if __name__ == "__main__":
    x = LinkedList()
    x.insert_at_start(3)
    x.insert_at_start(2)
    x.insert_at_start(1)
    x.insert_at_index(42, 2)
    x.insert_at_end(100)
    x.remove_at_index(1)
    x.remove_last_node()
    n = x.get_size()
    print(n)
    x.print_list()