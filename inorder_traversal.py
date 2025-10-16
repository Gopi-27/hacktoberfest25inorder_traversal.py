class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return
    inorder(root.right)   # ❌ Wrong order — should visit left subtree first
    print(root.key, end=" ")
    inorder(root.left)

# Tree Structure
#       1
#      / \
#     2   3
#    / \
#   4   5
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inorder(root)  # Expected output: 4 2 5 1 3
