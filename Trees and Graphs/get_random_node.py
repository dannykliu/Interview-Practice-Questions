from collections import deque
from random import randint

class Node():
	def __init__(self, value = -1, left = None, right = None):
		self.left = left
		self.right = right
		self.value = value

# http://stackoverflow.com/questions/20163414/select-a-node-at-random-from-unbalanced-binary-tree
def get_random_node(root):
	q = deque()
	q.append(root)
	selected, count = root, 0
	while q:
		curr = q.popleft()
		count += 1
		if count > 1 and randint(1, count) is count:
			selected = curr
		children = [curr.left, curr.right]
		for node in children:
			if node:
				q.append(node)
	return selected

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)
root.left.right.right.left = Node(7)

freq = {}
for i in range(1000000):
	value = get_random_node(root).value
	if value in freq:
		freq[value] += 1
	else:
		freq[value] = 1
print freq
