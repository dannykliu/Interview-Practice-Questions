from collections import deque

class Node():
	def __init__(self, value = -1, left = None, right = None):
		self.left = left
		self.right = right
		self.value = value

# solution is slow, we traverse tree again every time
def on_side(root, node):
	if root is None: 
		return False 
	if root is node: 
		return True
	return on_side(root.left, node) or on_side(root.right, node)

# top down, O(n^2)
# break down into smaller subproblems 
def first_common_ancestor_top_down(root, a, b):
	if root is a or root is b:
		return root
	elif on_side(root.left, a) and on_side(root.left, b):
		return first_common_ancestor(root.left, a, b)
	elif on_side(root.right, a) and on_side(root.right, b):
		return first_common_ancestor(root.right, a, b)
	else:
		return root

# We traverse from the bottom, and once we reach a node which matches one of the two nodes, 
# we pass it up to its parent. The parent would then test its left and right subtree 
# if each contain one of the two nodes. If yes, then the parent must be the LCA 
# and we pass its parent up to the root. If not, we pass the lower node which 
# contains either one of the two nodes (if the left or right subtree contains either p or q),
# or NULL (if both the left and right subtree does not contain either p or q) up.

# solve the smaller subproblem first
# bottom up O(n)
def first_common_ancestor(root, a, b):
	if root is None: 
		return None
	if root is a or root is b:
		return root
	# following code only runs if we haven't found the node 
	left = first_common_ancestor(root.left, a, b)
	right = first_common_ancestor(root.right, a, b)
	if left and right: # one exists on both sides, diverges here
		return root
	# here, we found either a or b on only one sub-tree, return the non-null sub-tree
	if left: return left 
	if right: return right


root, a, b, c, d, e, f = Node('r'), Node('a'), Node('b'), Node('c'), Node('d'), Node('e'), Node('f')
root.right = c
root.left = b
b.left = d
b.right = e
c.left = f

print first_common_ancestor(root, d, b).value
