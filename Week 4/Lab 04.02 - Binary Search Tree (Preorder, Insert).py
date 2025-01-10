"""Lab 04.02 - Binary Search Tree (Preorder, Insert)"""

class BSTNode:
    def __init__(self, data: int = None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        pNew = BSTNode(data)

        if self.root is None:
            self.root = pNew
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = pNew
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = pNew
                        break
                    current = current.right

    def preorder(self):
        def _preorder(node):
            nonlocal result
            if node is not None:
                result += " -> "
                result += str(node.data)
                _preorder(node.left)
                _preorder(node.right)

        result = ""
        _preorder(self.root)
        print(result)

def main():
    my_bst = BST()
    for i in range(int(input())):
        my_bst.insert(int(input()))

    print("Preorder:", end="")
    my_bst.preorder()

main()