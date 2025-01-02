"""Lab 03.05 – Singly Linked List (Delete)"""

class DataNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None

    def insert_last(self, data):
        new_node = DataNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.count += 1
    
    def insert_front(self, data):
        new_node = DataNode(data)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def insert_before(self, node, data):
        new_node = DataNode(data)

        if self.head is None:
            print("Cannot insert, " + node + " does not exist.")
            return

        if self.head.data == node:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        previous = None

        while current is not None and current.data != node:
            previous = current
            current = current.next

        if current is None:
            print("Cannot insert, " + node + " does not exist.")
            return

        previous.next = new_node
        new_node.next = current
    
    def delete(self, data):
        if self.head is None:
            print("Cannot delete, " + data + " does not exist.")
            return

        if self.head.data == data:
            self.head = self.head.next
            self.count -= 1
            return

        current = self.head
        previous = None

        while current is not None and current.data != data:
            previous = current
            current = current.next

        if current is None:
            print("Cannot delete, " + data + " does not exist.")
            return

        previous.next = current.next
        self.count -= 1

    def traverse(self):
        if self.count == 0:
            print("This is an empty list.")
        else:
            output = ""
            node = self.head
            while node is not None:
                output += node.data
                node = node.next
                if node is not None:
                    output += " -> "
            print(output)

def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        text = input()
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        elif condition == "B":
            mylist.insert_before(*data.split(", "))
        elif condition == "D":
           mylist.delete(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()

main()