from collections import deque
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# Create a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Your level_order_traversal function
class Solution:
    def level_order_traversal(self, root):
        if root is None:
            return []
        
        result = []
        q = deque()
        q.append(root)

        while q:
            curr = q.popleft()
            result.append(curr.val)

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        return result

# Test your function
solution = Solution()
print(solution.level_order_traversal(root))  # Expected output: [1, 2, 3, 4, 5, 6, 7]
