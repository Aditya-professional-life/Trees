from collections import deque

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None



def isBalanced(root):
    if root == None:
        return 0
    
    lh = isBalanced(root.left)
    rh = isBalanced(root.right)
    if lh == -1:
        return -1
    if rh == -1:
        return -1
    
    if abs(lh-rh)>1:
        return -1
    
    return max(lh,rh)+1


def isBalancedmain(root):
    if isBalanced(root) == -1:
        return False
    return True