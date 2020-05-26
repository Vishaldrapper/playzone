# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def insertAfter(self,prev_node,new_data):
        if prev_node is None:
            print("Error in list traversal")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self,new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_data
            return
        last = self.head

        while(last.next):
            last = last.next

        last.next = new_node

    # Function to initialize head
    def __init__(self):
        self.head = None

    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()

# Basic linked list insertion
    # llist.head = Node(1)
    # second = Node(2)
    # third = Node(3)
    # fourth = Node(4)
    # llist.head.next = second  # Link first node with second
    # second.next = third  # Link second node with the third node
    # third.next = fourth

    llist.push(25)
    llist.append(26)
    llist.insertAfter(llist.head.next,27)
    llist.append(28)
    llist.append(29)

    llist.printList()