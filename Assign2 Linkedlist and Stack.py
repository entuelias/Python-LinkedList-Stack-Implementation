class Node:
    """
    Represents a node in a singly linked list.
    """

    def __init__(self, data):
        """
        Initializes a new Node with the given data and sets the next node to None.

        :param data: The data to be stored in the node
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    Represents a singly linked list.
    """

    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.head = None

    def insertAtPos(self, data, pos):
        """
        Inserts a new node with the given data at the specified position.

        :param data: The data for the new node
        :param pos: The position to insert the new node (1-based index)
        """
        new_node = Node(data)
        if pos < 1:
            print("Position should be 1 or greater")
            return

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        for _ in range(pos - 2):
            if current is None:
                print("Position out of range")
                return
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def deleteAtPosition(self, pos):
        """
        Deletes the node at the specified position.

        :param pos: The position of the node to delete (1-based index)
        """
        if pos < 1:
            print("Position should be 1 or greater")
            return

        if self.head is None:
            print("List is empty")
            return

        if pos == 1:
            self.head = self.head.next
            return

        current = self.head
        for _ in range(pos - 2):
            if current is None or current.next is None:
                print("Position out of range")
                return
            current = current.next

        if current.next is None:
            print("Position out of range")
            return

        current.next = current.next.next

    def deleteAfterNode(self, prev_node_data):
        """
        Deletes the node that occurs after a node with the specified data.

        :param prev_node_data: The data of the node after which to delete the next node
        """
        current = self.head
        while current and current.data != prev_node_data:
            current = current.next

        if current is None or current.next is None:
            print("No node found or no node to delete after the given node")
            return

        current.next = current.next.next

    def searchNode(self, data):
        """
        Searches for a node with the specified data in the linked list.

        :param data: The data to search for
        :return: True if the node is found, False otherwise
        """
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        """
        Displays the content of the linked list.
        """
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


class Stack:
    """
    Represents a stack data structure using a singly linked list.
    """

    def __init__(self):
        """
        Initializes an empty stack.
        """
        self.top = None

    def push(self, data):
        """
        Pushes a new element onto the stack.

        :param data: The data to push onto the stack
        """
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """
        Pops the top element from the stack.

        :return: The data from the popped node
        """
        if self.top is None:
            print("Stack is empty")
            return None
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    def peek(self):
        """
        Returns the top element of the stack without removing it.

        :return: The data of the top node
        """
        if self.top is None:
            print("Stack is empty")
            return None
        return self.top.data

    def isEmpty(self):
        """
        Checks if the stack is empty.

        :return: True if the stack is empty, False otherwise
        """
        return self.top is None

    def display(self):
        """
        Displays the content of the stack.
        """
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example

# LinkedList Operations
linked1 = LinkedList()
linked1.insertAtPos(10, 1)
linked1.insertAtPos(20, 2)
linked1.insertAtPos(30, 3)
linked1.display()  # Output: 10 -> 20 -> 30 -> None

linked1.insertAtPos(25, 3)
linked1.display()  # Output: 10 -> 20 -> 25 -> 30 -> None

linked1.deleteAtPosition(2)
linked1.display()  # Output: 10 -> 25 -> 30 -> None

linked1.deleteAfterNode(25)
linked1.display()  # Output: 10 -> 25 -> None

print(linked1.searchNode(25))  # Output: True
print(linked1.searchNode(50))  # Output: False

# Stack Operations
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()  # Output: 3 -> 2 -> 1 -> None

print(stack.peek())  # Output: 3
print(stack.pop())  # Output: 3
stack.display()  # Output: 2 -> 1 -> None

print(stack.isEmpty())  # Output: False
stack.pop()
stack.pop()
print(stack.isEmpty())  # Output: True

# to access the docstrings in class,function or method you can use the format below as a example
# print(Stack.__doc__)