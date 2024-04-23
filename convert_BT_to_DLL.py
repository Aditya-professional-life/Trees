from collections import deque

class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.key = key

prev = None
def Convert(root):
    global prev
    if root == None:
        return root
    
    head = Convert(root.left)
    
    if prev is None:
        head = root
    else:
        prev.right = root
        root.left = prev

    prev = root

    Convert(root.right)  # Handling the right subtree
    
    return head  # Returning the head of the doubly linked list

# Function to print the doubly linked list
def printList(head):
    while head:
        print(head.key, end=" ")
        head = head.right

# Create a binary tree
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.right = Node(20)

# Convert the binary tree to a doubly linked list
head = Convert(root)

# Print the doubly linked list
print("Doubly linked list:")
printList(head)
