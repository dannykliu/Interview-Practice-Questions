from collections import deque


class Node:
    def __init__(self, value):
        self.adjacent = []
        self.visited = False
        self.value = value


def path_exists(start, dest):
    """
    to find path length, use tup (node, dist)
    to trace actual path, use a dictionary to keep track of where you came from
    """
    q, path = deque(), {}
    q.append(start)  # q.append((start, 0))
    start.visited = True
    while q:
        curr = q.popleft()
        if curr is dest:
            print("Found path!")
            return path
        for node in curr.adjacent:
            if not node.visited:
                node.visited = True
                path[node.value] = curr.value
                q.append(node)  # q.append((node, curr[1]+1))
    return -1


G = {'a': ['b'],
     'b': ['c', 'd']}

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
a.adjacent.append(b)
b.adjacent.append(c)
b.adjacent.append(d)

print(path_exists(a, d))
