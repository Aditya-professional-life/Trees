from collections import deque
class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.key = key

def printLevel(root):
    if root == None:
        return 
    q = deque()
    q.append(root)

    while len(q)>0:
        count = len(q)
        for i in range(count):
            curr = q.popleft()
            print(curr.key,end = " ")
            if curr.left is not None:
                q.append(curr.left)

            if curr.right is not None:
                q.append(curr.right)


        print()





root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)


printLevel(root)