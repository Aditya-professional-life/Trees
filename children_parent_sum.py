from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def SumProperty(root):
    if root is None or (root.left is None and root.right is None):
        return 1
    left_sum = right_sum = 0

    if root.left is not None:
        left_sum = root.left.data

    if root.right is not None:
        right_sum = root.right.data

    if (root.data == left_sum + right_sum) and SumProperty(root.left) and SumProperty(root.right):
        return 1

    return 0

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)

result = SumProperty(root)
print(result)
