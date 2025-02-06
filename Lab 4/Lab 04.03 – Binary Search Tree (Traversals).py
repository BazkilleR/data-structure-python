"""Lab 04.03 – Binary Search Tree (Traversals)"""

class BSTNode:
    def __init__(self, data: int = None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

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
        return result
    
    def inorder(self):
        def _preorder(node):
            nonlocal result
            if node is not None:
                _preorder(node.left)
                result += " -> "
                result += str(node.data)
                _preorder(node.right)

        result = ""
        _preorder(self.root)
        return result
    
    def postorder(self):
        def _preorder(node):
            nonlocal result
            if node is not None:
                _preorder(node.left)
                _preorder(node.right)
                result += " -> "
                result += str(node.data)

        result = ""
        _preorder(self.root)
        return result
    
    def traverse(self):
        if self.root == None:
            print("This is an empty binary search tree.")
        else:
            print("Preorder:" + self.preorder())
            print("Inorder:" + self.inorder())
            print("Postorder:" + self.postorder())

def main():
    my_bst = BST()
    for i in range(int(input())):
        my_bst.insert(int(input()))
    my_bst.traverse()

main()