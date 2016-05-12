class Node():
	def __init__(self, value = -1, left = None, right = None):
		self.left = left
		self.right = right
		self.value = value

# nodes will be returned bottom up but can think of solving problem as top down 
def helper(arr, start, end): # think of top down recursion
	if start > end: 
		return None
	mid_index = (start+end)/2
	root = Node(arr[mid_index]) # find the node
	root.left = helper(arr, start, mid_index-1) # find node.left
	root.right = helper(arr, mid_index +1, end) # find node.right
	return root # think of returning node first 

def minimal_tree(arr):
	return helper(arr, 0, len(arr)-1)

