from collections import deque
import math

class Node():
	def __init__(self, value = -1, left = None, right = None):
		self.left = left
		self.right = right
		self.value = value

# iterative
def check_balanced(root): # keep track of depth of each node with [node, depth]
	q, list_of_depths = deque(), []
	q.append([root, 0]) 
	while q:
		curr = q.popleft()
		children = [curr[0].left, curr[0].right]
		for node in children:
			if node:
				q.append([node, curr[1]+1])	
				# if we're at a leaf node, add it's height to the list
				if node.left is None or node.right is None:
					list_of_depths.append(curr[1]+1)
	# now check if any heights differ by more than 1
	print list_of_depths
	return (max(list_of_depths) - min(list_of_depths) <= 1)

# top down. already calculated the heights
# if the height of any node without 2 children minus the maximum height is greater than 1, return false
def helper_td(root, max_height = [0]):
	if root[0]:
		if root[1] > max_height[0]:
			max_height[0] = root[1]
		left = helper_td((root[0].left, root[1]+1), max_height)
		right = helper_td((root[0].right, root[1] +1), max_height)
		if (left is False or right is False 
			or (root[0].left is None or root[0].right is None 
				and max_height[0] - root[1] > 1)):
			return False
		return True

def balanced_td(root):
	return helper_td((root, 1))

root = Node(1)
root.left = Node(1)
root.right= Node(1)
root.left.left= Node(1)
root.left.right= Node(1)
root.left.left.left = Node(1)
root.right.right = Node(1)

print check_balanced(root)
print balanced_recurse(root)
print balanced_td(root)


