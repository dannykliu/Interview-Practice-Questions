import sys

class Node():
	def __init__(self, value = -1, left = None, right = None):
		self.left = left
		self.right = right
		self.value = value

# BC
# take care of BC
# RC
# could also copy values into array with in-order traversal, then check if array is sorted
def validate_bst(root, _min = -sys.maxint, _max = sys.maxint):
	if root is None: 
		return True 
	if (_min < root.value < _max) is False: 
		return False  
	return (validate_bst(root.left, _min, root.value) and 
		validate_bst(root.right, root.value, _max))

root = Node(3)
root.right = Node(4)
root.right.left = Node(2)

print validate_bst(root)
