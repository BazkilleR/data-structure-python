"""Lab 04.01 - Create BSTNode"""
class BSTNode:
    def __init__(self, data: int=None):
        """ > w < """
        self.data = data
        self.left = None
        self.right = None

def main():
    t1 = BSTNode(int(input()))
    print(t1.data)
    print(t1.left)
    print(t1.right)

main()