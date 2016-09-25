import sys
from collections import deque

class ThreeInOne: # idea to use a wrapper class and keep a separate array for the sizes
	def __init__(self, stack_capacity):
		self.array = [None]*3*stack_capacity
		self.stack_capacity = stack_capacity
		self.sizes = [0]*3

	def push(self, stack_num, value):
		if(self.sizes[stack_num-1] >= self.stack_capacity):
			print "Error, max stack stack_capacity!"; return
		self.sizes[stack_num-1] += 1
		self.array[self.stack_capacity*(stack_num-1) + self.sizes[stack_num-1] -1] = value

	def pop(self, stack_num):
		if(self.sizes[stack_num-1] == 0): 
			print "Error, popping from empty stack!"; return
		value = self.array[self.stack_capacity*(stack_num-1) + self.sizes[stack_num-1] -1]
		self.array[self.stack_capacity*(stack_num-1) + self.sizes[stack_num-1] -1] = None
		self.sizes[stack_num-1] -= 1
		return value

class MinStack: # idea that you only need the history of the smallest values
	def __init__(self):
		self.stack = []
		self.min = sys.maxint
		self.minArray = []

	def push(self, value):
		self.stack.append(value)
		if(value <= self.min): 
			self.min = value
			self.minArray.append(value)

	def _min(self):
		if(len(self.stack) == 0): print "Stack is empty!"; return
		return self.minArray[len(self.minArray)-1]

	def pop(self):
		if(len(self.stack) == 0): print "Stack is empty!"; return
		value = self.stack.pop()
		if(value == self.minArray[len(self.minArray)-1]): 
			self.minArray.pop()
		return value

class SetOfStacks: # trick to use array of deques for pop_at()
	def __init__(self, capacity):
		self.capacity = capacity
		self.arrStack = [deque()]

	def push(self, value):
		if(len(self.arrStack[len(self.arrStack)-1]) == self.capacity):
			self.arrStack.append(deque([value])) # cool deque literal
		else:
			self.arrStack[len(self.arrStack)-1].append(value)

	def pop(self):
		if(len(self.arrStack) == 0): print "Error, empty stack!"; return
		value = self.arrStack[len(self.arrStack)-1].pop()
		if(len(self.arrStack[len(self.arrStack)-1]) == 0):
			self.arrStack.pop()
		return value

	def pop_at(self, index):
		if(index > len(self.arrStack) -1): print "Error, invalid index!"; return
		value = self.arrStack[index].pop()
		for i in range(index+1, len(self.arrStack)-1, 1):
			self.arrStack[i-1].append(self.arrStack[i].popleft())
		return value

class myQueue:
	def __init__(self):
		stack = []
		queue = []
	def push(self, value):
		stack.append(value)
	def pop(self):
		if(len(queue) == 0 and len(stack) == 0): print "Error, empty stack!"; return
		if(len(queue) == 0):
			while(len(stack) != 0):
				queue.append(stack.pop())
		return queue.pop()

def sort_stack(stack): # idea to use a temp variable and temp stack then reverse
	if(len(stack) == 0): print "Error, empty stack!"; return
	temp_stack, temp_val = [], 0 
	temp_stack.append(stack.pop())
	while stack:
		if(stack[len(stack)-1] > temp_stack[len(temp_stack)-1]):
			temp_stack.append(stack.pop())
		else:
			temp_val = stack.pop()
			while(temp_stack and temp_stack[len(temp_stack)-1] > temp_val):
				stack.append(temp_stack.pop())
			temp_stack.append(temp_val)
			
	while temp_stack:
		stack.append(temp_stack.pop())

class Dog:
	spieces = "Dog"
	def __init__(self, name):
		self.name = name
class Cat:
	spieces = "Cat"
	def __init__(self, name):
		self.name = name

class AnimalShelter:
	time_stamp = 0 # idea to use a timestamp and 2 separate queues 
	def __init__(self):
		self.dogs = deque()
		self.cats = deque()

	def enque(self, animal):
		AnimalShelter.time_stamp += 1 # use of static variable
		if(animal.spieces == "Dog"):
			self.dogs.append((animal, AnimalShelter.time_stamp)) # deque of tuples
		elif(animal.spieces == "Cat"): 
			self.cats.append((animal, time_stamp))
		else: print "Invalid animal!"; return

	def dequeDog(self): return self.dogs.popleft()[0]
	def dequeCat(self): return self.cats.popLeft()[0]

	def dequeAny(self):
		if(len(self.cats) == 0 and len(self.dogs) == 0): print "Error, no animals!"; return
		elif(len(self.cats) == 0): return self.dogs.popleft()[0]
		elif(len(self.dogs) == 0): return self.cats.popleft()[0]
		elif(self.cats[0][1] < self.dogs[0][1]): return self.cats.popleft()[0]
		else: return self.dogs.popleft()[0]

d1 = Dog("A")
d2 = Dog("B")
c1 = Dog("C")
c2 = Dog("D")

shelter = AnimalShelter()
shelter.enque(d1)
shelter.enque(c1)
shelter.enque(d2)
shelter.enque(c2)

print shelter.dequeAny().name, shelter.dequeAny().name, shelter.dequeAny().name, shelter.dequeAny().name




