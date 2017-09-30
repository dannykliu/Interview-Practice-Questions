from collections import deque


class Node:
    def __init__(self, value=-1, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


# iterative
def check_balanced(root):  # keep track of depth of each node with [node, depth]
    q, list_of_depths = deque(), []
    q.append([root, 0])
    while q:
        curr = q.popleft()
        children = [curr[0].left, curr[0].right]
        for node in children:
            if node:
                q.append([node, curr[1] + 1])
                # if we're at a leaf node, add it's height to the list
                if node.left is None and node.right is None:
                    list_of_depths.append(curr[1] + 1)
    # now check if any heights differ by more than 1
    print(list_of_depths)
    return max(list_of_depths) - min(list_of_depths) <= 1


# OR or AND in the conditional??
def helper_td(root, heights):
    if root[0]:
        if root[0].left is None and root[0].right is None:
            heights.append(root[1])
        helper_td((root[0].left, root[1] + 1), heights)
        helper_td((root[0].right, root[1] + 1), heights)
        return heights


def balanced_td(root):
    heights = helper_td((root, 1), [])
    return max(heights) - min(heights) <= 1


root = Node(1)
root.left = Node(1)
root.right = Node(1)
root.left.left = Node(1)
root.left.right = Node(1)
root.left.left.left = Node(1)
root.right.right = Node(1)

print(check_balanced(root))
print(balanced_td(root))
