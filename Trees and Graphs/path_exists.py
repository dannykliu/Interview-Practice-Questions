from collections import deque

class Node():
	def __init__(self, value):
		self.adjacent = []
		self.visited = False
		self.value = value
	
def path_exists(start, dest): # to find path length, use tup (node, dist)
	q, path = deque(), {} # to trace actual path, use a dictionary
	# want dictionary to keep track of where you came from 
	q.append(start) # q.append((start, 0))
	start.visited = True
	while q:
		curr = q.popleft() 
		if curr is dest: print "Found path!"; return path
		for node in curr.adjacent:
			if node.visited == False:
				node.visited = True
				path[node] = curr 
				q.append(node) # q.append((node, curr[1]+1))
	return -1





