import Stack

def main():
    my_stack = Stack.Stack()
    my_stack.push(1)
    my_stack.push("Two")
    my_stack.push(3.0)
    print(my_stack.pop())  # Output: 3
    print(my_stack.peek())  # Output: 2
    print(my_stack.get_size())  # Output: 2

main()

