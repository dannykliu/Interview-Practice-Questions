from collections import deque


class Node:
    def __init__(self, value=-1, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


# bottom up soooo goood
def max_depth(root):
    if root is None:
        return 0
    left = max_depth(root.left)
    right = max_depth(root.right)
    return (left if left > right else right) + 1


# will modify preorder param but not inorder
def make_tree1(inorder, preorder):
    if len(inorder) is 0 or len(preorder) is 0:
        return None
    root = Node(preorder[0])
    index = inorder.index(preorder[0])
    preorder.pop(0)
    # preorder = preorder[1:] doesn't work because it makes a copy of preorder
    # preorder.pop(0) changes the reference of 'preorder' in memory
    root.left = make_tree1(inorder[:index], preorder)
    root.right = make_tree1(inorder[index + 1:], preorder)
    return root


def make_tree2(inorder, postorder):
    if len(inorder) is 0 or len(postorder) is 0:
        return None
    # works because reference of preorder is changed in memory
    root = Node(postorder[len(postorder) - 1])
    index = inorder.index(postorder[len(postorder) - 1])
    postorder.pop()
    root.right = make_tree2(inorder[index + 1:], postorder)
    root.left = make_tree2(inorder[:index], postorder)
    return root


def in_order(root, arr=[]):
    if root is not None:
        in_order(root.left, arr)
        arr.append(root)
        in_order(root.right, arr)


def pre_order(root, arr=[]):
    if root is not None:
        arr.append(root)
        pre_order(root.left, arr)
        pre_order(root.right, arr)


# Theorem: Elements between 2 given elements in an inorder traversal
# contains the lowest common ancestor of those 2 elements
# preorder gives you the roots of the subtrees
# inorder tells you what's to the left and right of the subtree of your selected element is the root
def lowest_common_ancestor(root, node1, node2):
    in_order_arr = in_order(root)
    pre_order_arr = pre_order(root)
    # find first element in preorder arr that has node1 on left and node2 on right in the inorder arr
    for x in pre_order_arr:
        index_lca, index_node1, index_node2 = 0, 0, 0
        for i in range(in_order_arr):
            if in_order_arr[i] == node1:
                index_node1 = i
            if in_order_arr[i] == node2:
                index_node2 = i
            if in_order_arr[i] == x:
                index_lca = i
        if index_node1 < index_lca < index_node2:
            return x


# take care of base cases. think about edge cases at the root
def lca(root, node1, node2):
    if node1 is None or node2 is None:
        return None  # error
    if node1 is node2:
        return node1
    if root is None:
        return None
    if root is (node1 or node2):
        return root
    left = lca(root.left, node1, node2)
    right = lca(root.right, node1, node2)
    if left and right:
        return root
    if left or right:
        return left or right
    else:
        return None


# watch out for glitches with tuples
def all_sums_from_root(root):
    sums, q, last_sum = {}, deque(), 0
    q.append((root, last_sum))
    while q:
        curr = q.popleft()
        val = curr[0].value + curr[1]
        if val not in sums:
            sums[val] = 1
        else:
            sums[val] += 1
        children = [(curr[0].left, val), (curr[0].right, val)]
        for tup in children:
            if tup[0]:
                q.append(tup)
    return sums


# store diameter, pass up height
def helper(root, diameter=[0]):
    if root is None:
        return 0
    left = helper(root.left, diameter)
    right = helper(root.right, diameter)
    if (left + right + 1) > diameter[0]:
        diameter[0] = left + right + 1
    return (left if left > right else right) + 1


def find_diameter(root):
    diameter = [0]
    helper(root, diameter)
    return diameter[0]


# bottom up dp so good
# [4] = 2[0][3] + 2[1][2]
# [5] = 2[0][4] + 2[1][3] + [2][2]
def count_number_of_binary_trees(num):
    arr = [1, 1, 2, 5]
    while len(arr) <= num:
        start = 0
        end = len(arr) - 1
        next_index = 0
        while end > start:
            next_index += 2 * arr[start] * arr[end]
            start += 1
            end -= 1
        if end == start:
            next_index += arr[start] * arr[end]
        arr.append(next_index)
    return arr  # arr[num]


# print count_number_of_binary_trees(10)

root = Node(10)
root.left = Node(4)
root.right = Node(6)
root.right.right = Node(30)
root.right.right.right = Node(31)
root.right.left = Node(2)
root.right.left.left = Node(1)
root.right.left.right = Node(2)


# print find_diameter(root)

def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.value)
        print_tree(root.right)


root2 = make_tree1([10, 30, 40, 50, 60, 70, 90], [50, 30, 10, 40, 70, 60, 90])
# print_tree(root2)
root2 = make_tree2([10, 30, 40, 50, 60, 70, 90], [10, 40, 30, 60, 90, 70, 50])
print_tree(root2)
# print max_depth(root)

# print all_sums_from_root(root)
