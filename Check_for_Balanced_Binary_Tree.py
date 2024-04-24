class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.key = key

def isBalanced(root):
    if root is None:
        return 0
    
    lh = isBalanced(root.left)
    if lh == -1:
        return -1
    
    rh = isBalanced(root.right)
    if rh == -1:
        return -1
    
    if abs(lh - rh) > 1:
        return -1
    return max(lh, rh) + 1

def isBalancedMain(root):
    if isBalanced(root) == -1:
        return False
    return True

# Example usage:
if __name__ == "__main__":
    # Create a sample binary tree
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.right = Node(20)

    # Check if the tree is balanced
    if isBalancedMain(root):
        print("The binary tree is balanced.")
    else:
        print("The binary tree is not balanced.")
