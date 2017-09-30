class Node:
    def __init__(self, value=-1, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


def weave(llst, rlst, perm, answer=[]):
    if llst == [] and rlst == []:  # llst is [] does not work!!
        perm.append(answer)
    if llst:
        ans = answer + [llst[0]]  # list concatenation
        weave(llst[1:], rlst, perm, ans)
    if rlst:
        ans = answer + [rlst[0]]
        weave(llst, rlst[1:], perm, ans)


def bst_sequences(root):
    if root is None:
        return None
    left = bst_sequences(root.left)
    right = bst_sequences(root.right)
    if left is None and right is None:
        return [[root.value]]  # very bottom
    if left and right:
        lst = []
        # mash permutations together but keep their relative order
        # catches all permutations. Perm(left) x Perm(right)
        for llst in left:
            for rlst in right:
                weave(llst, rlst, lst)
        for i in range(len(lst)):
            lst[i] = [root.value] + lst[i]
        return lst
    if left or right:
        lst = left if left else right
        for i in range(len(lst)):
            lst[i] = [root.value] + lst[i]
        return lst


root = Node(0)
root.left = Node(-2)
root.right = Node(2)
root.left.left = Node(-3)
root.left.right = Node(-1)
root.right.left = Node(1)
root.right.right = Node(3)

print(len(bst_sequences(root)))
# lst = []
# weave([1], [3], lst)
# print lst
# lst = []
# weave([1, 2], [3, 4], lst)
# print lst
