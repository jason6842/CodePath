# Problem 4
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def sum_inventory(inventory):
    if not inventory:
        return 0
    
    left_sum = sum_inventory(inventory.left)
    right_sum = sum_inventory(inventory.right)
    
    return left_sum + right_sum + inventory.val

"""
     40
    /  \
   5   10
  /   /  \
20   1   30
"""

inventory = TreeNode(40, 
                    TreeNode(5, TreeNode(20)),
                            TreeNode(10, TreeNode(1), TreeNode(30)))

print(sum_inventory(inventory))

def calculate_yield(root):
    # Base case: if it's a leaf node, return its value
    if not root.left and not root.right:
        return root.val
    
    # Goes all the way to the left
    # Then goes all the way to the right
    # We have 4 and 2, then as we are going back up the tree, we hit a '-' node,
    # so we match one of the operator conditions.
    # Since we have a left and right value, we return 4 - 2
    # (Note: we're still in the left function call)

    # Now we go back to the root, but then we go to the right subtree,
    # going all the way to the left = 10 and right = 2.
    # Moving back up, we reach the '*' operator and compute 10 * 2.
    # So now the right = 10 * 2, and we move back up to compute 2 + 20 = 22.

    left = calculate_yield(root.left)
    right = calculate_yield(root.right)

    if root.val == "+":
        return left + right
    elif root.val == "-":
        return left - right
    elif root.val == "*":
        return left * right


"""
      +
     / \ 
    /   \
   -     *
  / \   / \
 4   2 10  2
"""

root = TreeNode("+")
root.left = TreeNode("-")
root.right = TreeNode("*")
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(2)

print(calculate_yield(root))