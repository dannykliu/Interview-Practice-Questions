from collections import deque

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

def print_list(head):
	curr = head
	while(curr != None):
		print curr.val
		curr = curr.next

# Tips: If checking for curr.next != null, adjust curr.next
# curr.next is used when we need to adjust the links
# If checking curr != null, adjust curr
def remove_dups(head): 
	my_set, curr, prev = set(), head, None
	while(curr != None):
		if(curr.val not in my_set):
			my_set.add(curr.val)
			prev = curr # idea to keep track of prev node
			# need prev because we're not always deleting the immediate next node
		else:
			prev.next = curr.next
		curr = curr.next

def remove_dups_no_temp_buffer(head):
	curr = head
	while(curr != None):
		runner = curr
		while(runner.next != None):
			if(runner.next.val == curr.val): # idea to check NEXT node's value
				runner.next = runner.next.next
			else:
				runner = runner.next
		curr = curr.next

def kth_to_last(head, k):
	curr, runner = head, head
	for i in range(k): 
		runner = runner.next # idea to have a runner node
		if(runner == None): return None # out of bounds
	while(runner != None):
		curr = curr.next
		runner = runner.next
	return curr

def delete_middle_node(node):
	if(node == None or node.next == None): return False
	node.next.val = node.val # idea to copy the value of the next node
	node.next = node.next.next
	return True

def partition(head, value):
	curr, queue = head, deque # idea to use queue
	while(curr != None):
		if(curr.val >= value):
			queue.append(curr)
		elif(curr.val < value and len(queue) != 0):
			swap = queue.popleft() # copy values
			temp = swap.val
			swap.val = curr.val
			curr.val = temp
		curr = curr.next

# Trick: Keep track of the carry bit of both lists
# Extended: Set first carry-bit to 0 so that when you add it first time, it does nothing
def sum_lists(list1, list2):
	if(list1 == None): return list2
	if(list2 == None): return list1
	new_list, carry, sum = None, 0, 0
	curr1 = list1
	curr2 = list2
	sum = curr1.val + curr2.val
	if(sum >= 10):
		carry = 1
		sum = sum % 10
	else: carry = 0
	new_list = Node(sum)
	curr1 = curr1.next
	curr2 = curr2.next
	curr_new = new_list

	while(curr1 != None and curr2 != None):
		sum = curr1.val + curr2.val + carry
		if(sum >= 10):
			carry = 1
			sum = sum % 10
		else: carry = 0
		newNode = Node(sum)
		curr_new.next = newNode
		curr_new = curr_new.next
		curr1 = curr1.next
		curr2 = curr2.next

	if(curr1 == None and curr2 == None and carry == 1):
		newNode = Node(sum)
		curr_new.next = newNode
	elif(curr1 == None and curr2 == None and carry == 0):
		return new_list 
	elif(curr1 == None):
		curr2.val += carry
		curr_new.next = curr2
	elif(curr2 == None):
		curr1.val += carry
		curr_new.next = curr1
	return new_list

def palindrome(head): # idea to use stack and runner node to find middle node
	curr, runner, stack = head, head, [] 
	while(runner != None and runner.next != None):
		runner = runner.next.next
		stack.append(curr.val)
		curr = curr.next
	if(runner != None): # trap, dealing with even and odd number of nodes
		curr = curr.next
	while(curr != None):
		if(stack.pop() != curr.val):
			return False
		curr = curr.next
	return True

def intersection(list1, list2):
	if(list1 == None or list2 == None): return None
	curr1, curr2, len1, len2 = list1, list2, 1, 1
	while(curr1.next != None):
		len1 += 1
		curr1 = curr1.next
	while(curr2.next != None):
		len2 += 1
		curr2 = curr2.next
	# check if last nodes are the same
	if(curr1 != curr2): return None
	curr1, curr2 = list1, list2
	# advance shorter list by difference in length
	if(len1 < len2):
		for i in range(len2 - len1):
			curr2 = curr2.next
	elif(len2 < len1):
		for i in range(len1 - len2):
			curr1 = curr1.next
	while(curr1 != curr2):
		curr1 = curr1.next
		curr2 = curr2.next
	return curr1

def intersection_with_set(list1, list2): 
	curr1, curr2, nodes = list1, list2, set()
	while(curr1 != None or curr2 != None):
		if(curr1 in nodes): return curr1
		if(curr2 in nodes): return curr2
		nodes.add(curr1)
		nodes.add(curr2)
		if(curr1 != None): curr1 = curr1.next
		if(curr2 != None): curr2 = curr2.next
	return None

def loop_detection_with_set(head):
	curr, nodes = head, set()
	while(curr != None):
		if(curr in nodes): return curr
		nodes.add(curr)
		curr = curr.next
	return None

# if your second node is going twice as fast in a circular linklist, you will
# meet up at the start again. slight modification to detect loop 
def loop_detection(head):
	curr, runner = head, head
	while(runner != None and runner.next != None):
		runner = runner.next.next
		curr = curr.next
		if(curr == runner): break
	if(runner == None or runner.next == None): return False
	# move curr and runner to the same node
	curr = head
	while(curr != runner):
		curr = curr.next
		runner = runner.next
	return curr

# curr.next, prev node, copy values, runner nodes, stacks and queues, sets, mod 2

a = Node(7)
b = Node(1)
c = Node(6)
d = Node(100)
e = Node(6)
f = Node(1)
g = Node(7)

a1 = Node(1)
a2 = Node(2)
a1.next = a2
a2.next = d

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = d

print loop_detection(a).val



