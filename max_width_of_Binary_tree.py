from collections import deque

class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.key = key

def maxwidth(root):
    if root == None:
        return 0
    
    q = deque()
    q.append(root)

    res = 0
    while q:
        size = len(q)
        res = max(res, size)
        for i in range(size):
            curr = q.popleft()
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

    return res

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)

print("Maximum width:", maxwidth(root))
