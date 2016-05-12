class Node():
	def __init__(self, value = -1, left = None, right = None):
		self.left = left
		self.right = right
		self.value = value

def paths_with_sum(root, sums = {}):
	if root is None:
		return (None, None)
	left = paths_with_sum(root.left, sums)
	right = paths_with_sum(root.right, sums)
	# left contains the left node and all possible sums of the left subtree
	keys, lst_of_keys = [], []
	if left[0] and right[0]:
		keys = left[1] + right[1]
	elif left[0]:
		keys = left[1]
	elif right[0]:
		keys = right[1]
	for key in keys: 
		val = key + root.value
		lst_of_keys.append(val) # KEY LINE: 'val' reps all possible sums with root.value
		if val in sums.keys():
			sums[val] += 1
		else:
			sums[val] = 1
	# if left and right are None, we just do a simple update of that element only
	if root.value in sums.keys():
		sums[root.value] += 1
	else:
		sums[root.value] = 1
	lst_of_keys.append(root.value)
	return (root, lst_of_keys)

# all possible sums for 2nd lowest level depends on all possible sums for lowest level

root1 = Node(100)
root = Node(3)
root1.left = root

root.left = Node(1)
root.right = Node(4)
root.left.left = Node(-1)
#root.right.right = Node(5)

sums = {}
paths_with_sum(root1, sums)
print sums
