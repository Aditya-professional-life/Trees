class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.key = key


def isBalanced(root):
    if root == None:
        return 0
    
    lh = isBalanced(root.left)
    if lh == -1:
        return -1
    
    rh = isBalanced(root.right)
    if rh == -1:
        return -1
    
    if(abs(lh-rh)>1):
        return -1
    return max(lh,rh)+1

def isBalancedMain(root):
    if isBalanced(root)==-1:
        return False
    return True


if __name__ == '__main__':
	root = Node(10)
	root.left = Node(5)
	root.right = Node(30)
	root.right.left = Node(15)
	root.right.right = Node(20)
	if (isBalanced(root) == -1):
		print("Not Balanced")
	else:
		print("Balanced")
