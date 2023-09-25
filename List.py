# import Node

class LinkedList:
    def __init__(self):
        # node = Node.Node()
        self.head = None

    def printer(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

    # def main():
    #     print("Imported Node")
    #     Node.node = 4