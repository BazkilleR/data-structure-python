"""Lab 03.03 – Singly Linked List (Insert "Front) """

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
        else:
            print("Invalid Condition!")
    mylist.traverse()

main()