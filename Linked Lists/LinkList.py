import queue


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def link_list(arr):
    head, prev = None, None
    for i in range(len(arr)):
        curr = Node(arr[i])
        if prev is not None:
            prev.next = curr
        else:
            head = curr
        prev = curr
    return head


def print_list(head):
    curr = head
    while curr is not None:
        if curr.next is not None:
            print("%d -> " % curr.val, end='')
        else:
            print(curr.val)
        curr = curr.next


def remove_dups(head):
    existing_values, curr, prev = set(), head, None
    while curr is not None:
        if curr.val not in existing_values:
            existing_values.add(curr.val)
            prev = curr  # idea to keep track of prev node
        else:
            prev.next = curr.next
        curr = curr.next
    print_list(head)
    return head


def remove_dups_no_temp_buffer(head):
    curr = head
    while curr is not None:
        runner, prev = curr.next, curr
        while runner is not None:
            if runner.val != curr.val:
                prev = runner
            else:
                prev.next = runner.next
            runner = runner.next
        curr = curr.next
    print_list(head)
    return head


def kth_to_last(head, k):
    curr, runner = head, head
    for i in range(k):
        runner = runner.next  # idea to have a runner node
        if runner is None:
            return None  # out of bounds
    while runner is not None:
        curr = curr.next
        runner = runner.next
    return curr


def delete_middle_node(node):
    if node is None or node.next is None:
        return False
    node.next.val = node.val  # idea to copy the value of the next node
    node.next = node.next.next
    return True


def partition(head, value):
    curr, q = head, queue.Queue()  # idea to use queue
    while curr is not None:
        if curr.val >= value:
            q.put(curr)
        elif curr.val < value and not q.empty():
            larger = q.get()
            temp = larger.val
            larger.val = curr.val
            curr.val = temp
            q.put(curr)
        curr = curr.next
    print_list(head)
    return head


def sum_lists_backwards(l1, l2, carry):
    if l1 is None and l2 is None:
        return None
    l1_val = l1.val if l1 is not None else 0
    l2_val = l2.val if l2 is not None else 0
    l1_next = l1.next if l1 is not None else None
    l2_next = l2.next if l2 is not None else None
    curr_sum = l1_val + l2_val + carry
    node = Node(curr_sum % 10)
    node.next = sum_lists_backwards(l1_next, l2_next, curr_sum > 9)
    return node


def sum_lists_forward_helper(l1, l2, prev=None):
    if l1 is None or l2 is None:
        return l1 or l2
    curr_sum = l1.val + l2.val
    if prev is not None:
        prev.val += curr_sum > 9
    node = Node(curr_sum % 10)
    node.next = sum_lists_forward_helper(l1.next, l2.next, node)
    return node


def get_length(head):
    if head is None:
        return 0
    return 1 + get_length(head.next)


def sum_lists_forward(l1, l2):
    length1, length2 = get_length(l1), get_length(l2)
    if length1 != length2:
        _shorter, longer = (l1, l2) if length1 < length2 else (l2, l1)
        shorter, prev = None, None
        for i in range(abs(length1 - length2)):
            node = Node(0)
            if shorter is None:
                shorter = node
                prev = shorter
            else:
                prev.next = node
            if i == abs(length1 - length2) - 1:
                node.next = _shorter
        return sum_lists_forward_helper(shorter, longer)
    else:
        return sum_lists_forward_helper(l1, l2)


def palindrome(head):  # idea to use stack and runner node to find middle node
    curr, runner, stack = head, head, queue.LifoQueue()
    while runner is not None and runner.next is not None:
        runner = runner.next.next
        stack.put(curr.val)
        curr = curr.next
    if runner is not None:  # trap, dealing with even and odd number of nodes
        curr = curr.next
    while curr is not None:
        if stack.get() != curr.val:
            return False
        curr = curr.next
    return True


def intersection(list1, list2):
    if list1 is None or list2 is None:
        return None
    curr1, curr2, len1, len2 = list1, list2, 1, 1
    while curr1.next is not None:
        len1 += 1
        curr1 = curr1.next
    while curr2.next is not None:
        len2 += 1
        curr2 = curr2.next
    # check if last nodes are the same
    if curr1 != curr2:
        return None
    curr1, curr2 = list1, list2
    # advance longer list by difference in length
    if len1 < len2:
        for i in range(len2 - len1):
            curr2 = curr2.next
    elif len2 < len1:
        for i in range(len1 - len2):
            curr1 = curr1.next
    while curr1 != curr2:
        curr1 = curr1.next
        curr2 = curr2.next
    return curr1


def intersection_with_set(list1, list2):
    curr1, curr2, nodes = list1, list2, set()
    while curr1 is not None or curr2 is not None:
        if curr1 in nodes:
            return curr1
        if curr2 in nodes:
            return curr2
        nodes.add(curr1)
        nodes.add(curr2)
        if curr1 is not None:
            curr1 = curr1.next
        if curr2 is not None:
            curr2 = curr2.next
    return None


def loop_detection_with_set(head):
    curr, nodes = head, set()
    while curr is not None:
        if curr in nodes:
            return curr
        nodes.add(curr)
        curr = curr.next
    return None


# if your second node is going twice as fast in a circular linklist, you will
# meet up at the start again. slight modification to detect loop 
def loop_detection(head):
    curr, runner = head, head
    while runner is not None and runner.next is not None:
        runner = runner.next.next
        curr = curr.next
        if curr == runner:
            break
    if runner is None or runner.next is None:
        return False
    # move curr and runner to the same node
    curr = head
    while curr != runner:
        curr = curr.next
        runner = runner.next
    return curr


# curr.next, prev node, copy values, runner nodes, stacks and queues, sets, mod 2

partition(link_list([10, 1, 5, 1, 2, 11, 3]), 5)
partition(link_list([10, 5, 1, 2, 3]), 5)
print_list(sum_lists_backwards(link_list([7, 1, 7]), link_list([5, 9, 2, 4]), 0))
print_list(sum_lists_backwards(link_list([]), link_list([5, 9, 2, 4]), 0))
print_list(sum_lists_forward(link_list([6, 1, 7]), link_list([2, 9, 5, 0])))
print(palindrome(link_list([1, 2, 3, 2, 1])))

