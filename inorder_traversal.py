class Node:
    def _init_(self, key):
        self.key = key
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return
    inorder(root.left)     # ✅ Visit left subtree first
    print(root.key, end=" ")
    inorder(root.right)    # ✅ Then visit right subtree

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

inorder(root)  # Output: 4 2 5 1 3
