class Node:
    def __init__(self, value=-1, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


# remember to define base case. top down
def same_tree(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.value == root2.value:
        return (same_tree(root1.left, root2.left)
                and same_tree(root1.right, root2.right))
    return False


# naive O(n**2) solution
def subtree(bt, st):
    if bt is None:
        return False
    if st is None:
        return True
    if same_tree(bt, st):
        return True
    return subtree(bt.left, st) or subtree(bt.right, st)


# good O(n) solution
def in_order(root, arr=[]):
    if root is not None:
        in_order(root.left, arr)
        arr.append(root.value)
        in_order(root.right, arr)


def post_order(root, arr=[]):
    if root is not None:
        post_order(root.left, arr)
        post_order(root.right, arr)
        arr.append(root.value)


# in-order and pre-order traversals uniquely identify a b-tree
def is_subtree(bt, st):
    if bt is None:
        return False
    if st is None:
        return True
    bt_io_arr, bt_po_arr = [], []
    st_io_arr, st_po_arr = [], []
    in_order(bt, bt_io_arr)
    post_order(bt, bt_po_arr)
    in_order(st, st_io_arr)
    post_order(st, st_po_arr)
    return (''.join(str(x) for x in st_io_arr) in ''.join(str(x) for x in bt_io_arr)
            and ''.join(str(x) for x in st_po_arr) in ''.join(str(x) for x in bt_po_arr))


root = Node(10)
root.left = Node(4)
root.right = Node(6)
root.left.right = Node(30)

root1 = Node(26)
root2 = root1
root1.left = Node(10)
root1.right = Node(3)
root1.right.right = Node(3)
root1.left.left = Node(4)
root1.left.left.right = Node(30)
root1.left.right = Node(6)

print(subtree(root1, root1.right))
