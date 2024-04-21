from collections import deque

class Solution:
    def __init__(self,data) -> None:
        self.left = None
        self.right = None
        self.data = data




def LeftView(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    q.append(None)

    while len(q) >1:
        curr = q.popleft()
        