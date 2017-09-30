import sys
from collections import deque


class ThreeInOne:  # idea to use a wrapper class and keep a separate array for the sizes
    def __init__(self, stack_capacity):
        self.array = [None] * 3 * stack_capacity
        self.stack_capacity = stack_capacity
        self.sizes = [0] * 3

    def push(self, stack_num, value):
        if self.sizes[stack_num - 1] >= self.stack_capacity:
            raise Exception("Error, max stack stack_capacity!")
        self.sizes[stack_num - 1] += 1
        self.array[self.stack_capacity * (stack_num - 1) + self.sizes[stack_num - 1] - 1] = value

    def pop(self, stack_num):
        if self.sizes[stack_num - 1] == 0:
            raise Exception("Error, popping from empty stack!")
        value = self.array[self.stack_capacity * (stack_num - 1) + self.sizes[stack_num - 1] - 1]
        self.array[self.stack_capacity * (stack_num - 1) + self.sizes[stack_num - 1] - 1] = None
        self.sizes[stack_num - 1] -= 1
        return value


class MinStack:  # idea that you only need the history of the smallest values
    def __init__(self):
        self.stack = []
        self.min = sys.maxint
        self.min_array = []

    def push(self, value):
        self.stack.append(value)
        if value <= self.min:
            self.min = value
            self.min_array.append(value)

    def _min(self):
        if len(self.stack) == 0:
            raise Exception("Stack is empty!")
        return self.min_array[-1]

    def pop(self):
        if len(self.stack) == 0:
            raise Exception("Stack is empty!")
        value = self.stack.pop()
        if value == self.min_array[-1]:
            self.min_array.pop()
        return value


class SetOfStacks:  # trick to use array of deques for pop_at()
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr_stack = [deque()]

    def push(self, value):
        if len(self.arr_stack[-1]) == self.capacity:
            self.arr_stack.append(deque([value]))  # cool deque literal
        else:
            self.arr_stack[-1].append(value)

    def pop(self):
        if len(self.arr_stack) == 0:
            raise Exception("Error, empty stack!")
        value = self.arr_stack[-1].pop()
        if len(self.arr_stack[-1]) == 0:
            self.arr_stack.pop()
        return value

    def pop_at(self, index):
        if index > len(self.arr_stack) - 1:
            raise Exception("Error, invalid index!")
        value = self.arr_stack[index].pop()
        for i in range(index + 1, len(self.arr_stack) - 1, 1):
            self.arr_stack[i - 1].append(self.arr_stack[i].popleft())
        return value


class QueueStack:
    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def push(self, val):
        self.push_stack.append(val)

    def pop(self):
        if len(self.pop_stack) > 0:
            return self.pop_stack.pop()
        elif len(self.push_stack) == 0:
            raise Exception("Empty queue!")
        else:  # pop_stack is empty but push_stack still has values
            self.pop_stack = self.push_stack[::-1]  # reverse stack
            self.push_stack = []
            return self.pop_stack.pop()


def sort_stack(stack):  # idea to use a temp variable and temp stack then reverse
    if len(stack) == 0:
        raise Exception("Empty stack!")
    temp_stack, temp_val = [], 0
    temp_stack.append(stack.pop())
    while stack:
        if stack[-1] > temp_stack[-1]:
            temp_stack.append(stack.pop())
        else:
            temp_val = stack.pop()
            while temp_stack and temp_stack[-1] > temp_val:
                stack.append(temp_stack.pop())
            temp_stack.append(temp_val)

    while temp_stack:
        stack.append(temp_stack.pop())


class Dog:
    species = "Dog"

    def __init__(self, name):
        self.name = name


class Cat:
    species = "Cat"

    def __init__(self, name):
        self.name = name


class AnimalShelter:
    time_stamp = 0  # idea to use a timestamp and 2 separate queues

    def __init__(self):
        self.dogs = deque()
        self.cats = deque()

    def enque(self, animal):
        AnimalShelter.time_stamp += 1  # use of static variable
        if animal.species == "Dog":
            self.dogs.append((animal, AnimalShelter.time_stamp))  # deque of tuples
        elif animal.species == "Cat":
            self.cats.append((animal, AnimalShelter.time_stamp))
        else:
            raise Exception("Invalid animal!")

    def deque_dog(self):
        return self.dogs.popleft()[0]

    def deque_cat(self):
        return self.cats.popLeft()[0]

    def deque_any(self):
        if len(self.cats) == 0 and len(self.dogs) == 0:
            raise Exception("No animals!")
        elif len(self.cats) == 0:
            return self.dogs.popleft()[0]
        elif len(self.dogs) == 0:
            return self.cats.popleft()[0]
        elif self.cats[0][1] < self.dogs[0][1]:
            return self.cats.popleft()[0]
        else:
            return self.dogs.popleft()[0]

# d1 = Dog("A")
# d2 = Dog("B")
# c1 = Dog("C")
# c2 = Dog("D")
#
# shelter = AnimalShelter()
# shelter.enque(d1)
# shelter.enque(c1)
# shelter.enque(d2)
# shelter.enque(c2)
#
# print(shelter.dequeAny().name, shelter.dequeAny().name, shelter.dequeAny().name, shelter.dequeAny().name)
