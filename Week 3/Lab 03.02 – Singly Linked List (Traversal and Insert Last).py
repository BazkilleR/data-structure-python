"""Lab 03.02 – Singly Linked List (Traversal and Insert Last)"""

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
        mylist.insert_last(input())
    mylist.traverse()

main()