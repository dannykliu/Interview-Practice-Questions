class Node:
    def __init__(self, value=-1, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


def successor_in_order_traversal(root):
    if root is None:
        return None
    if root.right:  # successor is left-most element of right subtree
        node = root.right
        while node.left:
            node = node.left
        return node
    else:  # no right subtree, search for first parent node with greater value
        node = root
        while node.parent:
            if node.parent.value >= node.value:
                return node.parent
            node = node.parent
        return root  # root is the biggest element


root, a, b, c, d, e, f = Node(10), Node(5), Node(15), Node(12), Node(13), Node(), Node()
root.parent = None
root.left = a
a.parent = root
root.right = b
b.parent = root
b.left = c
c.parent = b
c.right = d
d.parent = c
print(successor_in_order_traversal(root).value)
