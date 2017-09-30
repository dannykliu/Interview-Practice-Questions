from collections import deque


class Node:
    def __init__(self, value=-1, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


def level_order_traversal(root):
    q = deque()
    q.append(root)
    while q:
        curr = q.popleft()
        print(curr.value)
        this_level = [curr.left, curr.right]
        for node in this_level:
            if node:
                q.append(node)


def list_of_depths(root):  # use bfs on root and keep track of how many nodes we've added
    list_of_lists, nodes, q = [], [], deque()
    q.append(root)
    count, factor = 0, 1  # nice factor variable to count powers of 2
    while q:
        curr = q.popleft()
        nodes.append(curr)
        count += 1
        # create our linklist from nodes list
        if count == factor or len(q) == 0:
            for i in range(len(nodes)):
                if i != len(nodes) - 1:
                    nodes[i].next = nodes[i + 1]
                else:
                    nodes[-1].next = None
            list_of_lists.append(nodes[0])
            factor *= 2
            count, nodes = 0, []  # clear nodes only when finished traversing an entire level

        children = [curr.left, curr.right]
        for node in children:
            if node:
                q.append(node)
    return list_of_lists


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.right.right = Node(3)
root.right.right.right = Node(4)
root.left.left.left = Node(3.5)
linklist = list_of_depths(root)
for lst in linklist:
    curr = lst
    while curr:
        print(curr.value)
        curr = curr.next
