import Node
import List

# New Linked List
new_list = List.LinkedList()

# Set and create head node
new_list.head = Node.Node(1)

# Create following nodes
node_two = Node.Node(2)
node_three = Node.Node(3)

# Set following nodes
new_list.head.next = node_two
node_two.next = node_three

# Print the entire linked list
new_list.printer()